from pygogol.core import Request

from Defs import baseUrl

def delete(childId=None, folderId=None):
    url = baseUrl + "files/{folderId}/children/{childId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['childId', 'folderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(childId=None, folderId=None):
    url = baseUrl + "files/{folderId}/children/{childId}"
    method = "GET"
    return Request(
        method, 
        url.format(['childId', 'folderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(folderId=None, supportsTeamDrives=None):
    url = baseUrl + "files/{folderId}/children"
    method = "POST"
    return Request(
        method, 
        url.format(['folderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(folderId=None, maxResults=None, orderBy=None, pageToken=None, q=None):
    url = baseUrl + "files/{folderId}/children"
    method = "GET"
    return Request(
        method, 
        url.format(['folderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
