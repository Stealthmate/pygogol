from pygogol.core import Request

from Defs import baseUrl

def queryTestablePermissions():
    url = baseUrl + "v1/permissions:queryTestablePermissions"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
