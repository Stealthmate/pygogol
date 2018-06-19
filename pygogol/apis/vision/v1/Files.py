from pygogol.core import Request

from Defs import baseUrl

def asyncBatchAnnotate():
    url = baseUrl + "v1/files:asyncBatchAnnotate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
