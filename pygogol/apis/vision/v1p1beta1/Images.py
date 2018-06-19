from pygogol.core import Request

from Defs import baseUrl

def annotate():
    url = baseUrl + "v1p1beta1/images:annotate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
