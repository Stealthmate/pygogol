from pygogol.core import Request

from Defs import baseUrl

def check(clientRevision=None):
    url = baseUrl + "revisions/check"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
