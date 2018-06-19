from pygogol.core import Request

from Defs import baseUrl

def get(code=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/postalCodes/{code}"
    method = "GET"
    return Request(
        method, 
        url.format(['code', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/postalCodes"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
