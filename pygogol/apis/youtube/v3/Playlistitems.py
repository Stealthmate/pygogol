from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOfContentOwner=None):
    url = baseUrl + "playlistItems"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOfContentOwner=None, part=None):
    url = baseUrl + "playlistItems"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(id=None, maxResults=None, onBehalfOfContentOwner=None, pageToken=None, part=None, playlistId=None, videoId=None):
    url = baseUrl + "playlistItems"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None, part=None):
    url = baseUrl + "playlistItems"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
