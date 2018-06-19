from pygogol.core import Request

from Defs import baseUrl

def get(playerId=None, language=None):
    url = baseUrl + "players/{playerId}"
    method = "GET"
    return Request(
        method, 
        url.format(['playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(collection=None, language=None, maxResults=None, pageToken=None):
    url = baseUrl + "players/me/players/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['collection']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
