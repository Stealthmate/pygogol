from pygogol.core import Request

from Defs import baseUrl

def generatetags(profileId=None, campaignId=None, placementIds=None, tagFormats=None):
    url = baseUrl + "userprofiles/{profileId}/placements/generatetags"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/placements/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/placements"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, advertiserIds=None, archived=None, campaignIds=None, compatibilities=None, contentCategoryIds=None, directorySiteIds=None, groupIds=None, ids=None, maxEndDate=None, maxResults=None, maxStartDate=None, minEndDate=None, minStartDate=None, pageToken=None, paymentSource=None, placementStrategyIds=None, pricingTypes=None, searchString=None, siteIds=None, sizeIds=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/placements"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/placements"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/placements"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
