from pygogol.core import Request

from Defs import baseUrl

def delete(fileId=None, parentId=None):
    url = baseUrl + "files/{fileId}/parents/{parentId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['fileId', 'parentId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(fileId=None, parentId=None):
    url = baseUrl + "files/{fileId}/parents/{parentId}"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId', 'parentId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(fileId=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}/parents"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(fileId=None):
    url = baseUrl + "files/{fileId}/parents"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
