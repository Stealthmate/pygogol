from pygogol.core import Request

from Defs import baseUrl

def reset(questId=None):
    url = baseUrl + "quests/{questId}/reset"
    method = "POST"
    return Request(
        method, 
        url.format(['questId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAll():
    url = baseUrl + "quests/reset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAllForAllPlayers():
    url = baseUrl + "quests/resetAllForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetForAllPlayers(questId=None):
    url = baseUrl + "quests/{questId}/resetForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format(['questId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetMultipleForAllPlayers():
    url = baseUrl + "quests/resetMultipleForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
