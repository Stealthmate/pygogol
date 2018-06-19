from pygogol.core import Request

from Defs import baseUrl

def list(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/browsers"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
