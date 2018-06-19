from pygogol.core import Request

from Defs import baseUrl

def set(channelId=None, onBehalfOfContentOwner=None):
    url = baseUrl + "watermarks/set"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unset(channelId=None, onBehalfOfContentOwner=None):
    url = baseUrl + "watermarks/unset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
