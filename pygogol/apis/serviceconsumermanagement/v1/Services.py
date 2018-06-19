from pygogol.core import Request

from Defs import baseUrl

def search(parent=None, pageSize=None, pageToken=None, query=None):
    url = baseUrl + "v1/{+parent}:search"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
