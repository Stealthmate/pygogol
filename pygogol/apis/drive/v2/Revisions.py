from pygogol.core import Request

from Defs import baseUrl

def delete(fileId=None, revisionId=None):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['fileId', 'revisionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(fileId=None, revisionId=None):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId', 'revisionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(fileId=None, maxResults=None, pageToken=None):
    url = baseUrl + "files/{fileId}/revisions"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(fileId=None, revisionId=None):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['fileId', 'revisionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(fileId=None, revisionId=None):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['fileId', 'revisionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
