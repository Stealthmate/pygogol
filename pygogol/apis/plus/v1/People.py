from pygogol.core import Request

from Defs import baseUrl

def get(userId=None):
    url = baseUrl + "people/{userId}"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(collection=None, userId=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "people/{userId}/people/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['collection', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listByActivity(activityId=None, collection=None, maxResults=None, pageToken=None):
    url = baseUrl + "activities/{activityId}/people/{collection}"
    method = "GET"
    return Request(
        method, 
        url.format(['activityId', 'collection']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search(language=None, maxResults=None, pageToken=None, query=None):
    url = baseUrl + "people"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
