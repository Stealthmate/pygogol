from pygogol.core import Request

from Defs import baseUrl

def search(pageSize=None, pageToken=None):
    url = baseUrl + "v1/services:search"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
