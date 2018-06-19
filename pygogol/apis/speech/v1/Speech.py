from pygogol.core import Request

from Defs import baseUrl

def longrunningrecognize():
    url = baseUrl + "v1/speech:longrunningrecognize"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def recognize():
    url = baseUrl + "v1/speech:recognize"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
