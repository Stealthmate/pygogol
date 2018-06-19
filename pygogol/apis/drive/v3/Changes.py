from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def getStartPageToken(supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes/startPageToken"
    method = "GET"
    queryParams = {
        "supportsTeamDrives": supportsTeamDrives
		, "teamDriveId": teamDriveId
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )

def list(includeCorpusRemovals=None, includeRemoved=None, includeTeamDriveItems=None, pageSize=None, pageToken=None, restrictToMyDrive=None, spaces=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes"
    method = "GET"
    queryParams = {
        "includeCorpusRemovals": includeCorpusRemovals
		, "includeRemoved": includeRemoved
		, "includeTeamDriveItems": includeTeamDriveItems
		, "pageSize": pageSize
		, "pageToken": pageToken
		, "restrictToMyDrive": restrictToMyDrive
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

def watch(channel, includeCorpusRemovals=None, includeRemoved=None, includeTeamDriveItems=None, pageSize=None, pageToken=None, restrictToMyDrive=None, spaces=None, supportsTeamDrives=None, teamDriveId=None):
    url = baseUrl + "changes/watch"
    method = "POST"
    queryParams = {
        "includeCorpusRemovals": includeCorpusRemovals
		, "includeRemoved": includeRemoved
		, "includeTeamDriveItems": includeTeamDriveItems
		, "pageSize": pageSize
		, "pageToken": pageToken
		, "restrictToMyDrive": restrictToMyDrive
		, "spaces": spaces
		, "supportsTeamDrives": supportsTeamDrives
		, "teamDriveId": teamDriveId
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps(channel)
    )
