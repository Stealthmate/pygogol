from pygogol.core import Request

from Defs import baseUrl

def get(commentId=None):
    url = baseUrl + "comments/{commentId}"
    method = "GET"
    return Request(
        method, 
        url.format(['commentId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(activityId=None):
    url = baseUrl + "activities/{activityId}/comments"
    method = "POST"
    return Request(
        method, 
        url.format(['activityId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(activityId=None, maxResults=None, pageToken=None, sortOrder=None):
    url = baseUrl + "activities/{activityId}/comments"
    method = "GET"
    return Request(
        method, 
        url.format(['activityId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
