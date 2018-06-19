from pygogol.core import Request

from Defs import baseUrl

def reset(achievementId=None):
    url = baseUrl + "achievements/{achievementId}/reset"
    method = "POST"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAll():
    url = baseUrl + "achievements/reset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAllForAllPlayers():
    url = baseUrl + "achievements/resetAllForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetForAllPlayers(achievementId=None):
    url = baseUrl + "achievements/{achievementId}/resetForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetMultipleForAllPlayers():
    url = baseUrl + "achievements/resetMultipleForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
