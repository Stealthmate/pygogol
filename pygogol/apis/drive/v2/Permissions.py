from pygogol.core import Request

from Defs import baseUrl

def delete(fileId=None, permissionId=None, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['fileId', 'permissionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(fileId=None, permissionId=None, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId', 'permissionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIdForEmail(email=None):
    url = baseUrl + "permissionIds/{email}"
    method = "GET"
    return Request(
        method, 
        url.format(['email']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(fileId=None, emailMessage=None, sendNotificationEmails=None, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(fileId=None, maxResults=None, pageToken=None, supportsTeamDrives=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(fileId=None, permissionId=None, removeExpiration=None, supportsTeamDrives=None, transferOwnership=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['fileId', 'permissionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(fileId=None, permissionId=None, removeExpiration=None, supportsTeamDrives=None, transferOwnership=None, useDomainAdminAccess=None):
    url = baseUrl + "files/{fileId}/permissions/{permissionId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['fileId', 'permissionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
