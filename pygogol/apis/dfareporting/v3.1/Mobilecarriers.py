from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/mobileCarriers/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/mobileCarriers"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
