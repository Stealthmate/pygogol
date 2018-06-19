from pygogol.core import Request

from Defs import baseUrl

def cancel(name=None):
    url = baseUrl + "v1/operations/{+name}:cancel"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(name=None):
    url = baseUrl + "v1/operations/{+name}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v1/operations/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, name=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/operations"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
