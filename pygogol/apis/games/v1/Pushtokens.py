from pygogol.core import Request

from Defs import baseUrl

def remove():
    url = baseUrl + "pushtokens/remove"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update():
    url = baseUrl + "pushtokens"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
