from pygogol.core import Request

from Defs import baseUrl

def analyze():
    url = baseUrl + "v2beta1/dataSource:analyze"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
