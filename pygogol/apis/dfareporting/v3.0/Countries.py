from pygogol.core import Request

from Defs import baseUrl

def get(dartId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/countries/{dartId}"
    method = "GET"
    return Request(
        method, 
        url.format(['dartId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/countries"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
