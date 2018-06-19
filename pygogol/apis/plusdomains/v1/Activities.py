from pygogol.core import Request

from Defs import baseUrl

def get(activityId=None):
    url = baseUrl + "activities/{activityId}"
    method = "GET"
    return Request(
        method, 
        url.format(['activityId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(userId=None, preview=None):
    url = baseUrl + "people/{userId}/activities"
    method = "POST"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(collection=None, userId=None, maxResults=None, pageToken=None):
    url = baseUrl + "people/{userId}/activities/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['collection', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
