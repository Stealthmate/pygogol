from pygogol.core import Request

from Defs import baseUrl

def asyncrecognize():
    url = baseUrl + "v1beta1/speech:asyncrecognize"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def syncrecognize():
    url = baseUrl + "v1beta1/speech:syncrecognize"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
