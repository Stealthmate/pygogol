from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOfContentOwner=None):
    url = baseUrl + "playlists"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None):
    url = baseUrl + "playlists"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(channelId=None, hl=None, id=None, maxResults=None, mine=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, pageToken=None, part=None):
    url = baseUrl + "playlists"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None, part=None):
    url = baseUrl + "playlists"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
