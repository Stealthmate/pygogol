from glob import glob
from json import load
from os import path, sep
from pathlib import Path
import generate.template as TEMPLATE
from .util import *

PACKAGE_ROOT = "./"

def genDefs(js):
    scopes = []
    if "auth" in js and "oauth2" in js["auth"] and "scopes" in js["auth"]["oauth2"]:
        scopes = js["auth"]["oauth2"]["scopes"]
        scopes = list(map( lambda x: (x.split("/")[-1].upper().replace(".", "_").replace("-", "_"), x), scopes.keys()))
        
    return TEMPLATE.DEFS_JINJA.render(
        baseUrl = js["baseUrl"],
        scopes=scopes)

def genResourceMethod(name, js):
    pathParams = []
    queryParams = []
    bodyParam = None
    if "parameters" in js:
        params = js["parameters"].keys()
        pathParams = list(filter(lambda x: js["parameters"][x]["location"] == "path", params))
        queryParams = list(filter(lambda x: js["parameters"][x]["location"] == "query", params))
    if "request" in js and "$ref" in js["request"]:
        bodyParam = js["request"]["$ref"]
    return TEMPLATE.METHOD_JINJA.render(
        methodName=name, 
        httpMethod=js["httpMethod"],
        pathParams=pathParams,
        queryParams=queryParams,
        bodyParam=bodyParam,
        methodUrl=js["path"] or js["flatPath"])

def genResource(apiname, name, js):
    result = {}
    if "resources" in js:
        result = { k: genResource(apiname, k, js["resources"][k]) for k in js["resources"].keys() }
    if "methods" in js:
        result["__generated"] = TEMPLATE.RESOURCE_JINJA.render(
            apiname=apiname,
            methods=list(map(lambda x: genResourceMethod(x[0], x[1]), js["methods"].items()))
        )
    return result

def genSDK(path, apiname, js):
    res = genResource(apiname, apiname, js)
    res["defs"] = genDefs(js)
    return res

def generate():
    sdks = glob(PACKAGE_ROOT + "google-api-go-client/**/*-api.json", recursive=True)
    for s in sdks:
        p = path.normpath(s).split(sep)[1:]
        apiname = sep.join(p[:-1])
        print("Generating", apiname)
        if apiname == "sheets\\v4" or True:  
            sdkpath = Path("{}/pygogol/apis/{}".format(PACKAGE_ROOT, apiname)).resolve()
            with open(s, encoding="utf-8") as apidef:
                js = load(apidef)
                sdk = flatten(genSDK(sdkpath, apiname.replace("\\", ".").replace("-","_"), js))
                for f in sdk:
                    filepath = str(sdkpath).split(sep) + f[:-1]
                    filepath = [x for x in filepath if x != "__generated"]
                    filepath = sep.join(filepath[:-1] + [filepath[-1].capitalize()]) + ".py"
                    saveFile(filepath, f[-1])