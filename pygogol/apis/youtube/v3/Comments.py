from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "comments"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(part=None):
    url = baseUrl + "comments"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(id=None, maxResults=None, pageToken=None, parentId=None, part=None, textFormat=None):
    url = baseUrl + "comments"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def markAsSpam(id=None):
    url = baseUrl + "comments/markAsSpam"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setModerationStatus(banAuthor=None, id=None, moderationStatus=None):
    url = baseUrl + "comments/setModerationStatus"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(part=None):
    url = baseUrl + "comments"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
