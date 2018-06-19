from pygogol.core import Request

from Defs import baseUrl

def list(maxResults=None, pageToken=None):
    url = baseUrl + "adclients"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
