from pygogol.core import Request

from Defs import baseUrl

def get(profileId=None):
    url = baseUrl + "userprofiles/{profileId}"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "userprofiles"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
