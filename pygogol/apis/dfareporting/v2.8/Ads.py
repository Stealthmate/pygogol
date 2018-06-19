from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/ads/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/ads"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, active=None, advertiserId=None, archived=None, audienceSegmentIds=None, campaignIds=None, compatibility=None, creativeIds=None, creativeOptimizationConfigurationIds=None, dynamicClickTracker=None, ids=None, landingPageIds=None, maxResults=None, overriddenEventTagId=None, pageToken=None, placementIds=None, remarketingListIds=None, searchString=None, sizeIds=None, sortField=None, sortOrder=None, sslCompliant=None, sslRequired=None, type=None):
    url = baseUrl + "userprofiles/{profileId}/ads"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/ads"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/ads"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
