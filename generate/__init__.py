from subprocess import run
from glob import glob
from json import load
from itertools import chain
from os import path, sep
from pathlib import Path
import generate.template as TEMPLATE

PACKAGE_ROOT = "./"

def loadJSON(filepath):
    result = ""
    with open(filepath, encoding="utf-8") as f:
        result = load(f)
    return result

def formatScope(scope):
    name = scope.split("/")[-1]
    return "SCOPE_{NAME} = \"{VALUE}\"".format(NAME=name.upper().replace(".", "_").replace("-", "_"), VALUE=scope)

def genDefs(js):
    tt = TEMPLATE.DEFS.format(baseUrl=js["baseUrl"])
    if "auth" in js and "oauth2" in js["auth"] and "scopes" in js["auth"]["oauth2"]:
        scopes = js["auth"]["oauth2"]["scopes"]
        tt = tt + ( "\n\n" +  "\n".join( map( formatScope, scopes ) ))
    return tt

def genResourceMethod(i):
    name, js = i
    pathParams = []
    queryParams = []
    bodyParam = None
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
    tt = TEMPLATE.RESOURCE.format(
        resourceName=name, 
        params=", ".join(pathParams + (["{0}=None".format(bodyParam)] if bodyParam is not None else []) + list(map(defNone, queryParams))), 
        resourceUrl=js["path"], 
        resourceMethod=js["httpMethod"], 
        pathParams=", ".join(map(lambda x: "{0}={0}".format(x), pathParams)), 
        queryParams="\n\t\t, ".join(map(lambda x: "\"{0}\": {0}".format(x), queryParams)),
        bodyParam="dumps({})".format(bodyParam) if bodyParam else None)
    return tt

def genSDK(name, js):
    try:
        res = TEMPLATE.SDK + "\n\n" + "\n".join(map(genResourceMethod, js["methods"].items()))
        return res
    except KeyError as e:
        print("NOT OK!")
        print(js.keys())
        print("Skipping " + name)
    
def genModule(path, name, js):
    defs = genDefs(js)
    path.mkdir(exist_ok=True, parents=True)
    for rk, rv in js["resources"].items():
        if "resources" in rv:
            path_ = Path(str(path) + "\\" + rk)
            rv_ = dict(rv)
            rv_.update({
                "baseUrl": js["baseUrl"]
            })
            genModule(path_, rk, rv_)
        else:
            with open(str(path) + "\\" + "Defs.py", mode="w") as fdefs:
                fdefs.write(defs)
            res = genSDK(rk, rv)
            with open(str(path) + "\\{}.py".format(rk.capitalize()), mode="w") as fres:
                fres.write(res)

def generate():
    sdks = glob(PACKAGE_ROOT + "google-api-go-client/**/*-api.json", recursive=True)
    for s in sdks:
        p = path.normpath(s).split(sep)[1:]
        pp = sep.join(p[:-1])
        sdkpath = Path(PACKAGE_ROOT + "pygogol/apis/" + pp).resolve()
        with open(s, encoding="utf-8") as f:
            js = load(f)
            genModule(sdkpath, pp, js)