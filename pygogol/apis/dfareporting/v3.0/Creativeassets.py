from pygogol.core import Request

from Defs import baseUrl

def insert(advertiserId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/creativeAssets/{advertiserId}/creativeAssets"
    method = "POST"
    return Request(
        method, 
        url.format(['advertiserId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
