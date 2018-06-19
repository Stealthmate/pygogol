from pygogol.core import Request

from Defs import baseUrl

def listHidden(applicationId=None, maxResults=None, pageToken=None):
    url = baseUrl + "applications/{applicationId}/players/hidden"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
