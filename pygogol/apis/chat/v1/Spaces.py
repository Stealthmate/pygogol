from pygogol.core import Request

from Defs import baseUrl

def get(name=None):
    url = baseUrl + "v1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None):
    url = baseUrl + "v1/spaces"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
