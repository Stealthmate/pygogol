from pygogol.core import Request

from Defs import baseUrl

def copy(fileId=None, convert=None, ocr=None, ocrLanguage=None, pinned=None, supportsTeamDrives=None, timedTextLanguage=None, timedTextTrackName=None, visibility=None):
    url = baseUrl + "files/{fileId}/copy"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(fileId=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def emptyTrash():
    url = baseUrl + "files/trash"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def export(fileId=None, mimeType=None):
    url = baseUrl + "files/{fileId}/export"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generateIds(maxResults=None, space=None):
    url = baseUrl + "files/generateIds"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(fileId=None, acknowledgeAbuse=None, projection=None, revisionId=None, supportsTeamDrives=None, updateViewedDate=None):
    url = baseUrl + "files/{fileId}"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(convert=None, ocr=None, ocrLanguage=None, pinned=None, supportsTeamDrives=None, timedTextLanguage=None, timedTextTrackName=None, useContentAsIndexableText=None, visibility=None):
    url = baseUrl + "files"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(corpora=None, corpus=None, includeTeamDriveItems=None, maxResults=None, orderBy=None, pageToken=None, projection=None, q=None, spaces=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "files"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(fileId=None, addParents=None, convert=None, modifiedDateBehavior=None, newRevision=None, ocr=None, ocrLanguage=None, pinned=None, removeParents=None, setModifiedDate=None, supportsTeamDrives=None, timedTextLanguage=None, timedTextTrackName=None, updateViewedDate=None, useContentAsIndexableText=None):
    url = baseUrl + "files/{fileId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def touch(fileId=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}/touch"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def trash(fileId=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}/trash"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def untrash(fileId=None, supportsTeamDrives=None):
    url = baseUrl + "files/{fileId}/untrash"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(fileId=None, addParents=None, convert=None, modifiedDateBehavior=None, newRevision=None, ocr=None, ocrLanguage=None, pinned=None, removeParents=None, setModifiedDate=None, supportsTeamDrives=None, timedTextLanguage=None, timedTextTrackName=None, updateViewedDate=None, useContentAsIndexableText=None):
    url = baseUrl + "files/{fileId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(fileId=None, acknowledgeAbuse=None, projection=None, revisionId=None, supportsTeamDrives=None, updateViewedDate=None):
    url = baseUrl + "files/{fileId}/watch"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
