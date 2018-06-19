from pygogol.core import Request

from Defs import baseUrl

def get(leaderboardId=None, playerId=None, timeSpan=None, includeRankType=None, language=None, maxResults=None, pageToken=None):
    url = baseUrl + "players/{playerId}/leaderboards/{leaderboardId}/scores/{timeSpan}"
    method = "GET"
    return Request(
        method, 
        url.format(['leaderboardId', 'playerId', 'timeSpan']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(collection=None, leaderboardId=None, language=None, maxResults=None, pageToken=None, timeSpan=None):
    url = baseUrl + "leaderboards/{leaderboardId}/scores/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['collection', 'leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listWindow(collection=None, leaderboardId=None, language=None, maxResults=None, pageToken=None, resultsAbove=None, returnTopIfAbsent=None, timeSpan=None):
    url = baseUrl + "leaderboards/{leaderboardId}/window/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['collection', 'leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def submit(leaderboardId=None, language=None, score=None, scoreTag=None):
    url = baseUrl + "leaderboards/{leaderboardId}/scores"
    method = "POST"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def submitMultiple(language=None):
    url = baseUrl + "leaderboards/scores"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
