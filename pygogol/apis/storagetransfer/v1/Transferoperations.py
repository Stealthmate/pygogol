from pygogol.core import Request

from Defs import baseUrl

def cancel(name=None):
    url = baseUrl + "v1/{+name}:cancel"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(name=None):
    url = baseUrl + "v1/{+name}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(name=None, filter=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def pause(name=None):
    url = baseUrl + "v1/{+name}:pause"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resume(name=None):
    url = baseUrl + "v1/{+name}:resume"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
