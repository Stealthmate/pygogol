from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def create(fileId, permission, emailMessage=None, sendNotificationEmail=None, supportsTeamDrives=None, transferOwnership=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions"
    method = "POST"
    queryParams = {
        "emailMessage": emailMessage
		, "sendNotificationEmail": sendNotificationEmail
		, "supportsTeamDrives": supportsTeamDrives
		, "transferOwnership": transferOwnership
		, "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(permission)
    )

def delete(fileId, permissionId, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "DELETE"
    queryParams = {
        "supportsTeamDrives": supportsTeamDrives
		, "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId, permissionId=permissionId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def get(fileId, permissionId, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "GET"
    queryParams = {
        "supportsTeamDrives": supportsTeamDrives
		, "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId, permissionId=permissionId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(fileId, pageSize=None, pageToken=None, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions"
    method = "GET"
    queryParams = {
        "pageSize": pageSize
		, "pageToken": pageToken
		, "supportsTeamDrives": supportsTeamDrives
		, "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def update(fileId, permissionId, permission, removeExpiration=None, supportsTeamDrives=None, transferOwnership=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "PATCH"
    queryParams = {
        "removeExpiration": removeExpiration
		, "supportsTeamDrives": supportsTeamDrives
		, "transferOwnership": transferOwnership
		, "useDomainAdminAccess": useDomainAdminAccess
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format(fileId=fileId, permissionId=permissionId) + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(permission)
    )
