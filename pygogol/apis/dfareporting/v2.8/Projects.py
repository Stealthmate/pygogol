from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/projects/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, advertiserIds=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/projects"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
