from pygogol.core import Request

from Defs import baseUrl

def get(referenceSetId=None):
    url = baseUrl + "v1/referencesets/{referenceSetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['referenceSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/referencesets/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
