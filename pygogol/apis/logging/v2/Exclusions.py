from pygogol.core import Request

from Defs import baseUrl

def create(parent=None):
    url = baseUrl + "v2/{+parent}/exclusions"
    method = "POST"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(name=None):
    url = baseUrl + "v2/{+name}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v2/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(parent=None, pageSize=None, pageToken=None):
    url = baseUrl + "v2/{+parent}/exclusions"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(name=None, updateMask=None):
    url = baseUrl + "v2/{+name}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
