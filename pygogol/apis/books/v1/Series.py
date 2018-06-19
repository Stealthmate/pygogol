from pygogol.core import Request

from Defs import baseUrl

def get(series_id=None):
    url = baseUrl + "series/get"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
