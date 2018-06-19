from pygogol.core import Request

from Defs import baseUrl

def reset():
    url = baseUrl + "rooms/reset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetForAllPlayers():
    url = baseUrl + "rooms/resetForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
