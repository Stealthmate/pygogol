from pygogol.core import Request

from Defs import baseUrl

def delete(teamDriveId=None):
    url = baseUrl + "teamdrives/{teamDriveId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['teamDriveId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(teamDriveId=None, useDomainAdminAccess=None):
    url = baseUrl + "teamdrives/{teamDriveId}"
    method = "GET"
    return Request(
        method, 
        url.format(['teamDriveId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(requestId=None):
    url = baseUrl + "teamdrives"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None, q=None, useDomainAdminAccess=None):
    url = baseUrl + "teamdrives"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(teamDriveId=None):
    url = baseUrl + "teamdrives/{teamDriveId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['teamDriveId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
