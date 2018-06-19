from pygogol.core import Request

from Defs import baseUrl

def getConfig(name=None):
    url = baseUrl + "v1/{+name}/config"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateConfig(name=None):
    url = baseUrl + "v1/{+name}/config"
    method = "PATCH"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
