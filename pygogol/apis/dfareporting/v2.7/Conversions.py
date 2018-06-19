from pygogol.core import Request

from Defs import baseUrl

def batchinsert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/conversions/batchinsert"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
