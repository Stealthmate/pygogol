from pygogol.core import Request

from Defs import baseUrl

def get(name=None):
    url = baseUrl + "v1beta2/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, name=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1beta2/operations"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
