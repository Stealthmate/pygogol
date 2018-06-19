from subprocess import run
import glob
import json
from itertools import chain

sdks = glob.glob("./google-api-go-client/**/*-api.json", recursive=True)

def loadTemplate(fn):
    asd = ""
    with open(fn) as f:
        asd = f.read()
    return asd

templateSDK = loadTemplate("../template/SDK.py")
templateResource = loadTemplate("../template/Resource.py")
templateDefs = loadTemplate("../template/Defs.py")

from os import path, sep
from pathlib import Path

def formatScope(scope):
    name = scope.split("/")[-1]
    return "SCOPE_{NAME} = \"{VALUE}\"".format(NAME=name.upper().replace(".", "_").replace("-", "_"), VALUE=scope)

def genDefs(js):
    tt = templateDefs.format(baseUrl=js["baseUrl"])
    if "auth" in js and "oauth2" in js["auth"] and "scopes" in js["auth"]["oauth2"]:
        scopes = js["auth"]["oauth2"]["scopes"]
        tt = tt + ( "\n\n" +  "\n".join( map( formatScope, scopes ) ))
    return tt

def genResourceMethod(i):
    name, js = i
    pathParams = []
    queryParams = []
    bodyParam = "\"\""
    if "parameters" in js:
        params = js["parameters"].keys()
        pathParams = list(filter(lambda x: js["parameters"][x]["location"] == "path", params))
        queryParams = list(filter(lambda x: js["parameters"][x]["location"] == "query", params))
        fix = lambda x: "path_" + x.capitalize() if js["parameters"][x]["location"] == "path" else ("query_" + x)
        params = list(map(fix, params))
    else:
        params = []
    
    if "request" in js and "$ref" in js["request"]:
        bodyParam = js["request"]["$ref"].lower()
    defNone = lambda x: "{}=None".format(x)
    tt = templateResource.format(
        resourceName=name, 
        params=", ".join(pathParams + ([bodyParam] if bodyParam != "\"\"" else []) + list(map(defNone, queryParams))), 
        resourceUrl=js["path"], 
        resourceMethod=js["httpMethod"], 
        pathParams=", ".join(map(lambda x: "{0}={0}".format(x), pathParams)), 
        queryParams="\n\t\t, ".join(map(lambda x: "\"{0}\": {0}".format(x), queryParams)),
        bodyParam=bodyParam)
    return tt

def genResource(name, js):
    try:
        return templateSDK + "\n\n" + "\n".join(map(genResourceMethod, js["methods"].items()))
    except KeyError as e:
        print("Skipping " + name)


for s in sdks:
    p = path.normpath(s).split(sep)[2:]
    pp = sep.join(p[:-1])
    sdkpath = Path(str(Path.cwd()) + "./pygogol/apis/" + pp).resolve()
    sdkpath.mkdir(exist_ok=True, parents=True)
    if pp == "drive\\v3":
        print("DRIVE")
        with open(s, encoding="utf-8") as f:
            js = json.load(f)
            tt = genDefs(js)
            with open(str(sdkpath) + "\\" + "Defs.py", mode="w") as fdefs:
                fdefs.write(tt)
            for rk, rv in js["resources"].items():
                tt1 = genResource(rk, rv)
                if tt1:
                    with open(str(sdkpath) + "\\" + "{}.py".format(rk.capitalize()), mode="w") as fres:
                        fres.write(tt1)

            
 
    