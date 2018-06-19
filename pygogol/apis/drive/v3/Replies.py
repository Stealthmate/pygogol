from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def create(commentId, fileId, reply):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies"
    method = "POST"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(reply)
    )

def delete(commentId, fileId, replyId):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "DELETE"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId, replyId=replyId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def get(commentId, fileId, replyId, includeDeleted=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "GET"
    queryParams = {
        "includeDeleted": includeDeleted
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId, replyId=replyId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(commentId, fileId, includeDeleted=None, pageSize=None, pageToken=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies"
    method = "GET"
    queryParams = {
        "includeDeleted": includeDeleted
		, "pageSize": pageSize
		, "pageToken": pageToken
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def update(commentId, fileId, replyId, reply):
    url = baseUrl + "files/{fileId}/comments/{commentId}/replies/{replyId}"
    method = "PATCH"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId, replyId=replyId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(reply)
    )
