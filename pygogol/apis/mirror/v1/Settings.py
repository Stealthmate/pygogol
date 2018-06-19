from pygogol.core import Request

from Defs import baseUrl

def get(id=None):
    url = baseUrl + "settings/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
