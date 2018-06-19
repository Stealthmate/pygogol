from pygogol.core import Request

from Defs import baseUrl

def get(leaderboardId=None, language=None):
    url = baseUrl + "leaderboards/{leaderboardId}"
    method = "GET"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(language=None, maxResults=None, pageToken=None):
    url = baseUrl + "leaderboards"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
