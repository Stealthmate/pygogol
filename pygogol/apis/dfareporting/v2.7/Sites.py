from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/sites/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/sites"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, acceptsInStreamVideoPlacements=None, acceptsInterstitialPlacements=None, acceptsPublisherPaidPlacements=None, adWordsSite=None, approved=None, campaignIds=None, directorySiteIds=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None, subaccountId=None, unmappedSite=None):
    url = baseUrl + "userprofiles/{profileId}/sites"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/sites"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/sites"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
