from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, entity=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/acl/{entity}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket', 'entity', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, entity=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/acl/{entity}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'entity', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(bucket=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/acl"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bucket=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/acl"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, entity=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/acl/{entity}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket', 'entity', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, entity=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/acl/{entity}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket', 'entity', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
