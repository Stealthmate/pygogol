from pygogol.core import Request

from Defs import baseUrl

def checkIn(id=None):
    url = baseUrl + "v2alpha1/workers/{id}:checkIn"
    method = "POST"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
