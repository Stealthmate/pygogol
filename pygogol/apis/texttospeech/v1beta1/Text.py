from pygogol.core import Request

from Defs import baseUrl

def synthesize():
    url = baseUrl + "v1beta1/text:synthesize"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
