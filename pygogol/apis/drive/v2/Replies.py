from pygogol.core import Request

from Defs import baseUrl

def delete(commentId=None, fileId=None, replyId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['commentId', 'fileId', 'replyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(commentId=None, fileId=None, replyId=None, includeDeleted=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "GET"
    return Request(
        method, 
        url.format(['commentId', 'fileId', 'replyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(commentId=None, fileId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies"
    method = "POST"
    return Request(
        method, 
        url.format(['commentId', 'fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(commentId=None, fileId=None, includeDeleted=None, maxResults=None, pageToken=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies"
    method = "GET"
    return Request(
        method, 
        url.format(['commentId', 'fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(commentId=None, fileId=None, replyId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['commentId', 'fileId', 'replyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(commentId=None, fileId=None, replyId=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['commentId', 'fileId', 'replyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
