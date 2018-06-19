from pygogol.core import Request

from Defs import baseUrl

def addPeople(circleId=None, email=None, userId=None):
    url = baseUrl + "circles/{circleId}/people"
    method = "PUT"
    return Request(
        method, 
        url.format(['circleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(circleId=None):
    url = baseUrl + "circles/{circleId}"
    method = "GET"
    return Request(
        method, 
        url.format(['circleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(userId=None):
    url = baseUrl + "people/{userId}/circles"
    method = "POST"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(userId=None, maxResults=None, pageToken=None):
    url = baseUrl + "people/{userId}/circles"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(circleId=None):
    url = baseUrl + "circles/{circleId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['circleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def remove(circleId=None):
    url = baseUrl + "circles/{circleId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['circleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removePeople(circleId=None, email=None, userId=None):
    url = baseUrl + "circles/{circleId}/people"
    method = "DELETE"
    return Request(
        method, 
        url.format(['circleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(circleId=None):
    url = baseUrl + "circles/{circleId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['circleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
