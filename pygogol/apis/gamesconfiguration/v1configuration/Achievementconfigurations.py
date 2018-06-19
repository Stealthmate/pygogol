from pygogol.core import Request

from Defs import baseUrl

def delete(achievementId=None):
    url = baseUrl + "achievements/{achievementId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(achievementId=None):
    url = baseUrl + "achievements/{achievementId}"
    method = "GET"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(applicationId=None):
    url = baseUrl + "applications/{applicationId}/achievements"
    method = "POST"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(applicationId=None, maxResults=None, pageToken=None):
    url = baseUrl + "applications/{applicationId}/achievements"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(achievementId=None):
    url = baseUrl + "achievements/{achievementId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(achievementId=None):
    url = baseUrl + "achievements/{achievementId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
