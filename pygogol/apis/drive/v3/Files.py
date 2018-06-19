from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def copy(fileId, file, ignoreDefaultVisibility=None, keepRevisionForever=None, ocrLanguage=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}/copy"
    method = "POST"
    queryParams = {
        "ignoreDefaultVisibility": ignoreDefaultVisibility
		, "keepRevisionForever": keepRevisionForever
		, "ocrLanguage": ocrLanguage
		, "supportsTeamDrives": supportsTeamDrives
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(file)
    )

def create(file, ignoreDefaultVisibility=None, keepRevisionForever=None, ocrLanguage=None, supportsTeamDrives=None, useContentAsIndexableText=None):
    url = baseUrl + "files"
    method = "POST"
    queryParams = {
        "ignoreDefaultVisibility": ignoreDefaultVisibility
		, "keepRevisionForever": keepRevisionForever
		, "ocrLanguage": ocrLanguage
		, "supportsTeamDrives": supportsTeamDrives
		, "useContentAsIndexableText": useContentAsIndexableText
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(file)
    )

def delete(fileId, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}"
    method = "DELETE"
    queryParams = {
        "supportsTeamDrives": supportsTeamDrives
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def emptyTrash():
    url = baseUrl + "files/trash"
    method = "DELETE"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def export(fileId, mimeType=None):
    url = baseUrl + "files/{fileId}/export"
    method = "GET"
    queryParams = {
        "mimeType": mimeType
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def generateIds(count=None, space=None):
    url = baseUrl + "files/generateIds"
    method = "GET"
    queryParams = {
        "count": count
		, "space": space
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def get(fileId, acknowledgeAbuse=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}"
    method = "GET"
    queryParams = {
        "acknowledgeAbuse": acknowledgeAbuse
		, "supportsTeamDrives": supportsTeamDrives
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(corpora=None, corpus=None, includeTeamDriveItems=None, orderBy=None, pageSize=None, pageToken=None, q=None, spaces=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "files"
    method = "GET"
    queryParams = {
        "corpora": corpora
		, "corpus": corpus
		, "includeTeamDriveItems": includeTeamDriveItems
		, "orderBy": orderBy
		, "pageSize": pageSize
		, "pageToken": pageToken
		, "q": q
		, "spaces": spaces
		, "supportsTeamDrives": supportsTeamDrives
		, "teamDriveId": teamDriveId
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def update(fileId, file, addParents=None, keepRevisionForever=None, ocrLanguage=None, removeParents=None, supportsTeamDrives=None, useContentAsIndexableText=None):
    url = baseUrl + "files/{fileId}"
    method = "PATCH"
    queryParams = {
        "addParents": addParents
		, "keepRevisionForever": keepRevisionForever
		, "ocrLanguage": ocrLanguage
		, "removeParents": removeParents
		, "supportsTeamDrives": supportsTeamDrives
		, "useContentAsIndexableText": useContentAsIndexableText
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(file)
    )

def watch(fileId, channel, acknowledgeAbuse=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}/watch"
    method = "POST"
    queryParams = {
        "acknowledgeAbuse": acknowledgeAbuse
		, "supportsTeamDrives": supportsTeamDrives
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(channel)
    )
