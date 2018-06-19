from pygogol.core import Request

from Defs import baseUrl

def get(profileId=None, remarketingListId=None):
    url = baseUrl + "userprofiles/{profileId}/remarketingListShares/{remarketingListId}"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId', 'remarketingListId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, remarketingListId=None):
    url = baseUrl + "userprofiles/{profileId}/remarketingListShares"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/remarketingListShares"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
