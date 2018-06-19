from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def create(teamdrive, requestId=None):
    url = baseUrl + "teamdrives"
    method = "POST"
    queryParams = {
        "requestId": requestId
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(teamdrive)
    )

def delete(teamDriveId):
    url = baseUrl + "teamdrives/{teamDriveId}"
    method = "DELETE"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(teamDriveId=teamDriveId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def get(teamDriveId, useDomainAdminAccess=None):
    url = baseUrl + "teamdrives/{teamDriveId}"
    method = "GET"
    queryParams = {
        "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(teamDriveId=teamDriveId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(pageSize=None, pageToken=None, q=None, useDomainAdminAccess=None):
    url = baseUrl + "teamdrives"
    method = "GET"
    queryParams = {
        "pageSize": pageSize
		, "pageToken": pageToken
		, "q": q
		, "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def update(teamDriveId, teamdrive):
    url = baseUrl + "teamdrives/{teamDriveId}"
    method = "PATCH"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(teamDriveId=teamDriveId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(teamdrive)
    )
