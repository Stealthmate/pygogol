from pygogol.core import Request

from Defs import baseUrl

def getConfig(name=None):
    url = baseUrl + "v1/{+name}:getConfig"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def predict(name=None):
    url = baseUrl + "v1/{+name}:predict"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
