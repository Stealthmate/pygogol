from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, entity=None, userProject=None):
    url = baseUrl + "b/{bucket}/acl/{entity}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, entity=None, userProject=None):
    url = baseUrl + "b/{bucket}/acl/{entity}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(bucket=None, userProject=None):
    url = baseUrl + "b/{bucket}/acl"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bucket=None, userProject=None):
    url = baseUrl + "b/{bucket}/acl"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, entity=None, userProject=None):
    url = baseUrl + "b/{bucket}/acl/{entity}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, entity=None, userProject=None):
    url = baseUrl + "b/{bucket}/acl/{entity}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
