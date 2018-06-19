from pygogol.core import Request

from Defs import baseUrl

def run():
    url = baseUrl + "v2alpha1/pipelines:run"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
