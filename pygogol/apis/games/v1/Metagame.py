from pygogol.core import Request

from Defs import baseUrl

def getMetagameConfig():
    url = baseUrl + "metagameConfig"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listCategoriesByPlayer(collection=None, playerId=None, language=None, maxResults=None, pageToken=None):
    url = baseUrl + "players/{playerId}/categories/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['collection', 'playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
