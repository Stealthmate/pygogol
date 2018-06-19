from pygogol.core import Request

from Defs import baseUrl

def list(language=None, maxResults=None, pageToken=None):
    url = baseUrl + "achievements"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
