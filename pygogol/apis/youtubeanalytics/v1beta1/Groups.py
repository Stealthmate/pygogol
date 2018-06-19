from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOfContentOwner=None):
    url = baseUrl + "groups"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOfContentOwner=None):
    url = baseUrl + "groups"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(id=None, mine=None, onBehalfOfContentOwner=None, pageToken=None):
    url = baseUrl + "groups"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None):
    url = baseUrl + "groups"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
