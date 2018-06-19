from pygogol.core import Request

from Defs import baseUrl

def reset(leaderboardId=None):
    url = baseUrl + "leaderboards/{leaderboardId}/scores/reset"
    method = "POST"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAll():
    url = baseUrl + "scores/reset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAllForAllPlayers():
    url = baseUrl + "scores/resetAllForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetForAllPlayers(leaderboardId=None):
    url = baseUrl + "leaderboards/{leaderboardId}/scores/resetForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetMultipleForAllPlayers():
    url = baseUrl + "scores/resetMultipleForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
