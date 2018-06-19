from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/accountUserProfiles/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/accountUserProfiles"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, active=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None, subaccountId=None, userRoleId=None):
    url = baseUrl + "userprofiles/{profileId}/accountUserProfiles"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/accountUserProfiles"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/accountUserProfiles"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
