from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def delete(fileId, revisionId):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "DELETE"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId, revisionId=revisionId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def get(fileId, revisionId, acknowledgeAbuse=None):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "GET"
    queryParams = {
        "acknowledgeAbuse": acknowledgeAbuse
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId, revisionId=revisionId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(fileId, pageSize=None, pageToken=None):
    url = baseUrl + "files/{fileId}/revisions"
    method = "GET"
    queryParams = {
        "pageSize": pageSize
		, "pageToken": pageToken
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def update(fileId, revisionId, revision):
    url = baseUrl + "files/{fileId}/revisions/{revisionId}"
    method = "PATCH"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId, revisionId=revisionId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(revision)
    )
