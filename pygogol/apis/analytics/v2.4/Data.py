from pygogol.core import Request

from Defs import baseUrl

def get(dimensions=None, end-date=None, filters=None, ids=None, max-results=None, metrics=None, segment=None, sort=None, start-date=None, start-index=None):
    url = baseUrl + "data"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
