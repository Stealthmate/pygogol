from pygogol.core import Request

from Defs import baseUrl

def list(hl=None, maxResults=None, pageToken=None, part=None):
    url = baseUrl + "superChatEvents"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
