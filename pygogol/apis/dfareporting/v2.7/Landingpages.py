from pygogol.core import Request

from Defs import baseUrl

def delete(campaignId=None, id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/landingPages/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['campaignId', 'id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(campaignId=None, id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/landingPages/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['campaignId', 'id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(campaignId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/landingPages"
    method = "POST"
    return Request(
        method, 
        url.format(['campaignId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(campaignId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/landingPages"
    method = "GET"
    return Request(
        method, 
        url.format(['campaignId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(campaignId=None, profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/landingPages"
    method = "PATCH"
    return Request(
        method, 
        url.format(['campaignId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(campaignId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/landingPages"
    method = "PUT"
    return Request(
        method, 
        url.format(['campaignId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
