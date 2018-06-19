from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "timeline/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None):
    url = baseUrl + "timeline/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "timeline"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bundleId=None, includeDeleted=None, maxResults=None, orderBy=None, pageToken=None, pinnedOnly=None, sourceItemId=None):
    url = baseUrl + "timeline"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(id=None):
    url = baseUrl + "timeline/{id}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None):
    url = baseUrl + "timeline/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
