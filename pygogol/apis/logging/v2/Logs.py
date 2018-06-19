from pygogol.core import Request

from Defs import baseUrl

def delete(logName=None):
    url = baseUrl + "v2/{+logName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['logName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(parent=None, pageSize=None, pageToken=None):
    url = baseUrl + "v2/{+parent}/logs"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
