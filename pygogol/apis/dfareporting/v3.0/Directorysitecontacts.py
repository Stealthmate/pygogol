from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/directorySiteContacts/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, directorySiteIds=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/directorySiteContacts"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
