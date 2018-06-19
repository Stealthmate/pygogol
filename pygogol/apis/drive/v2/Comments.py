from pygogol.core import Request

from Defs import baseUrl

def delete(commentId=None, fileId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['commentId', 'fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(commentId=None, fileId=None, includeDeleted=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "GET"
    return Request(
        method, 
        url.format(['commentId', 'fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(fileId=None):
    url = baseUrl + "files/{fileId}/comments"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(fileId=None, includeDeleted=None, maxResults=None, pageToken=None, updatedMin=None):
    url = baseUrl + "files/{fileId}/comments"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(commentId=None, fileId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['commentId', 'fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(commentId=None, fileId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['commentId', 'fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
