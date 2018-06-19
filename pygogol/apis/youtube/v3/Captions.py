from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOf=None, onBehalfOfContentOwner=None):
    url = baseUrl + "captions"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def download(id=None, onBehalfOf=None, onBehalfOfContentOwner=None, tfmt=None, tlang=None):
    url = baseUrl + "captions/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOf=None, onBehalfOfContentOwner=None, part=None, sync=None):
    url = baseUrl + "captions"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(id=None, onBehalfOf=None, onBehalfOfContentOwner=None, part=None, videoId=None):
    url = baseUrl + "captions"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOf=None, onBehalfOfContentOwner=None, part=None, sync=None):
    url = baseUrl + "captions"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
