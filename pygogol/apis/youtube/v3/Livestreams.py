from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None):
    url = baseUrl + "liveStreams"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None):
    url = baseUrl + "liveStreams"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(id=None, maxResults=None, mine=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, pageToken=None, part=None):
    url = baseUrl + "liveStreams"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None):
    url = baseUrl + "liveStreams"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
