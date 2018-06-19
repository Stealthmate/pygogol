from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "liveChat/messages"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(part=None):
    url = baseUrl + "liveChat/messages"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(hl=None, liveChatId=None, maxResults=None, pageToken=None, part=None, profileImageSize=None):
    url = baseUrl + "liveChat/messages"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
