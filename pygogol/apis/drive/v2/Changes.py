from pygogol.core import Request

from Defs import baseUrl

def get(changeId=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes/{changeId}"
    method = "GET"
    return Request(
        method, 
        url.format(['changeId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getStartPageToken(supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes/startPageToken"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(includeCorpusRemovals=None, includeDeleted=None, includeSubscribed=None, includeTeamDriveItems=None, maxResults=None, pageToken=None, spaces=None, startChangeId=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(includeCorpusRemovals=None, includeDeleted=None, includeSubscribed=None, includeTeamDriveItems=None, maxResults=None, pageToken=None, spaces=None, startChangeId=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes/watch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
