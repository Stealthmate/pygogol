from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "liveChat/moderators"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(part=None):
    url = baseUrl + "liveChat/moderators"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(liveChatId=None, maxResults=None, pageToken=None, part=None):
    url = baseUrl + "liveChat/moderators"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
