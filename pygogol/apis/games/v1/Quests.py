from pygogol.core import Request

from Defs import baseUrl

def accept(questId=None, language=None):
    url = baseUrl + "quests/{questId}/accept"
    method = "POST"
    return Request(
        method, 
        url.format(['questId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(playerId=None, language=None, maxResults=None, pageToken=None):
    url = baseUrl + "players/{playerId}/quests"
    method = "GET"
    return Request(
        method, 
        url.format(['playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
