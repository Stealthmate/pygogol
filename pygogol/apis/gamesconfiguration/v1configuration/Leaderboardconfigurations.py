from pygogol.core import Request

from Defs import baseUrl

def delete(leaderboardId=None):
    url = baseUrl + "leaderboards/{leaderboardId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(leaderboardId=None):
    url = baseUrl + "leaderboards/{leaderboardId}"
    method = "GET"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(applicationId=None):
    url = baseUrl + "applications/{applicationId}/leaderboards"
    method = "POST"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(applicationId=None, maxResults=None, pageToken=None):
    url = baseUrl + "applications/{applicationId}/leaderboards"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(leaderboardId=None):
    url = baseUrl + "leaderboards/{leaderboardId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(leaderboardId=None):
    url = baseUrl + "leaderboards/{leaderboardId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['leaderboardId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
