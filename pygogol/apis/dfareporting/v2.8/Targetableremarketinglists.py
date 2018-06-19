from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/targetableRemarketingLists/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, active=None, advertiserId=None, maxResults=None, name=None, pageToken=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/targetableRemarketingLists"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
