from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/advertisers/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/advertisers"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, advertiserGroupIds=None, floodlightConfigurationIds=None, ids=None, includeAdvertisersWithoutGroupsOnly=None, maxResults=None, onlyParent=None, pageToken=None, searchString=None, sortField=None, sortOrder=None, status=None, subaccountId=None):
    url = baseUrl + "userprofiles/{profileId}/advertisers"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/advertisers"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/advertisers"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
