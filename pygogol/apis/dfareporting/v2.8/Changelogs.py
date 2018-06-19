from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/changeLogs/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, action=None, ids=None, maxChangeTime=None, maxResults=None, minChangeTime=None, objectIds=None, objectType=None, pageToken=None, searchString=None, userProfileIds=None):
    url = baseUrl + "userprofiles/{profileId}/changeLogs"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
