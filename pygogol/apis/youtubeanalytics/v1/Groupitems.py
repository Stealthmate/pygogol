from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOfContentOwner=None):
    url = baseUrl + "groupItems"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOfContentOwner=None):
    url = baseUrl + "groupItems"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(groupId=None, onBehalfOfContentOwner=None):
    url = baseUrl + "groupItems"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
