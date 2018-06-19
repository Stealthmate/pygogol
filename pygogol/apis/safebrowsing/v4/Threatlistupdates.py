from pygogol.core import Request

from Defs import baseUrl

def fetch():
    url = baseUrl + "v4/threatListUpdates:fetch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
