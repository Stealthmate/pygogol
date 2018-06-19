from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "liveChat/bans"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(part=None):
    url = baseUrl + "liveChat/bans"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
