from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/apps"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(appsId=None):
    url = baseUrl + "v1/apps/{appsId}"
    method = "GET"
    return Request(
        method, 
        url.format(['appsId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(appsId=None, updateMask=None):
    url = baseUrl + "v1/apps/{appsId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['appsId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def repair(appsId=None):
    url = baseUrl + "v1/apps/{appsId}:repair"
    method = "POST"
    return Request(
        method, 
        url.format(['appsId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
