from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/platformTypes/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/platformTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
