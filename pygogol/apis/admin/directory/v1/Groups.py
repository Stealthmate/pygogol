from pygogol.core import Request

from Defs import baseUrl

def delete(groupKey=None):
    url = baseUrl + "groups/{groupKey}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['groupKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(groupKey=None):
    url = baseUrl + "groups/{groupKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['groupKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "groups"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customer=None, domain=None, maxResults=None, orderBy=None, pageToken=None, query=None, sortOrder=None, userKey=None):
    url = baseUrl + "groups"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(groupKey=None):
    url = baseUrl + "groups/{groupKey}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['groupKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(groupKey=None):
    url = baseUrl + "groups/{groupKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['groupKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
