from pygogol.core import Request

from Defs import baseUrl

def query(profileId=None, maxResults=None, pageToken=None):
    url = baseUrl + "userprofiles/{profileId}/dimensionvalues/query"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
