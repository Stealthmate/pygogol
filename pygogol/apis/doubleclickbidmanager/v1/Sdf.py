from pygogol.core import Request

from Defs import baseUrl

def download():
    url = baseUrl + "sdf/download"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
