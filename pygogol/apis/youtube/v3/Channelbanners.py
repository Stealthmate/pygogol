from pygogol.core import Request

from Defs import baseUrl

def insert(channelId=None, onBehalfOfContentOwner=None):
    url = baseUrl + "channelBanners/insert"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
