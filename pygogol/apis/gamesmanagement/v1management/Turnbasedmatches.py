from pygogol.core import Request

from Defs import baseUrl

def reset():
    url = baseUrl + "turnbasedmatches/reset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetForAllPlayers():
    url = baseUrl + "turnbasedmatches/resetForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
