from pygogol.core import Request

from Defs import baseUrl

def list(databaseVersion=None):
    url = baseUrl + "flags"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
