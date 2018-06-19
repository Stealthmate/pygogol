from pygogol.core import Request

from Defs import baseUrl

def set(onBehalfOfContentOwner=None, videoId=None):
    url = baseUrl + "thumbnails/set"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
