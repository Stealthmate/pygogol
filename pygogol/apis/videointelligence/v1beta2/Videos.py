from pygogol.core import Request

from Defs import baseUrl

def annotate():
    url = baseUrl + "v1beta2/videos:annotate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )