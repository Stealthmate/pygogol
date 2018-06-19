from pygogol.core import Request

from Defs import baseUrl

def query():
    url = baseUrl + "freeBusy"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
