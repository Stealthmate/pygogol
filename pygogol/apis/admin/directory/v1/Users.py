from pygogol.core import Request

from Defs import baseUrl

def delete(userKey=None):
    url = baseUrl + "users/{userKey}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(userKey=None, customFieldMask=None, projection=None, viewType=None):
    url = baseUrl + "users/{userKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "users"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customFieldMask=None, customer=None, domain=None, event=None, maxResults=None, orderBy=None, pageToken=None, projection=None, query=None, showDeleted=None, sortOrder=None, viewType=None):
    url = baseUrl + "users"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def makeAdmin(userKey=None):
    url = baseUrl + "users/{userKey}/makeAdmin"
    method = "POST"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(userKey=None):
    url = baseUrl + "users/{userKey}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def undelete(userKey=None):
    url = baseUrl + "users/{userKey}/undelete"
    method = "POST"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(userKey=None):
    url = baseUrl + "users/{userKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(customFieldMask=None, customer=None, domain=None, event=None, maxResults=None, orderBy=None, pageToken=None, projection=None, query=None, showDeleted=None, sortOrder=None, viewType=None):
    url = baseUrl + "users/watch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
