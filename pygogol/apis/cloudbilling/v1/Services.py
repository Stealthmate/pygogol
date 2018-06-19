from pygogol.core import Request

from Defs import baseUrl

def list(pageSize=None, pageToken=None):
    url = baseUrl + "v1/services"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
