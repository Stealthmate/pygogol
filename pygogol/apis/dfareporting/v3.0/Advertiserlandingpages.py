from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/advertiserLandingPages/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/advertiserLandingPages"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, advertiserIds=None, archived=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None, subaccountId=None):
    url = baseUrl + "userprofiles/{profileId}/advertiserLandingPages"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/advertiserLandingPages"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/advertiserLandingPages"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
