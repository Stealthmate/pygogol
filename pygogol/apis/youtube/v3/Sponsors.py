from pygogol.core import Request

from Defs import baseUrl

def list(filter=None, maxResults=None, pageToken=None, part=None):
    url = baseUrl + "sponsors"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
