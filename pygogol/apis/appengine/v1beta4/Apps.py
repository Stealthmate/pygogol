from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1beta4/apps"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(appsId=None, ensureResourcesExist=None):
    url = baseUrl + "v1beta4/apps/{appsId}"
    method = "GET"
    return Request(
        method, 
        url.format(['appsId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(appsId=None, mask=None):
    url = baseUrl + "v1beta4/apps/{appsId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['appsId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
