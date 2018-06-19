from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def create(fileId, comment):
    url = baseUrl + "files/{fileId}/comments"
    method = "POST"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(comment)
    )

def delete(commentId, fileId):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "DELETE"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def get(commentId, fileId, includeDeleted=None):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "GET"
    queryParams = {
        "includeDeleted": includeDeleted
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(fileId, includeDeleted=None, pageSize=None, pageToken=None, startModifiedTime=None):
    url = baseUrl + "files/{fileId}/comments"
    method = "GET"
    queryParams = {
        "includeDeleted": includeDeleted
		, "pageSize": pageSize
		, "pageToken": pageToken
		, "startModifiedTime": startModifiedTime
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def update(commentId, fileId, comment):
    url = baseUrl + "files/{fileId}/comments/{commentId}"
    method = "PATCH"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(commentId=commentId, fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(comment)
    )
