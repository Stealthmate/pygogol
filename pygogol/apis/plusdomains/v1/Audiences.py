from pygogol.core import Request

from Defs import baseUrl

def list(userId=None, maxResults=None, pageToken=None):
    url = baseUrl + "people/{userId}/audiences"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
