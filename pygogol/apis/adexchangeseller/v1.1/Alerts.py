from pygogol.core import Request

from Defs import baseUrl

def list(locale=None):
    url = baseUrl + "alerts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
