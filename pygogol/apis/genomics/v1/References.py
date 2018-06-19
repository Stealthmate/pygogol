from pygogol.core import Request

from Defs import baseUrl

def get(referenceId=None):
    url = baseUrl + "v1/references/{referenceId}"
    method = "GET"
    return Request(
        method, 
        url.format(['referenceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/references/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
