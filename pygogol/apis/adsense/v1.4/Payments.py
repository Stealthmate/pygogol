from pygogol.core import Request

from Defs import baseUrl

def list():
    url = baseUrl + "payments"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
