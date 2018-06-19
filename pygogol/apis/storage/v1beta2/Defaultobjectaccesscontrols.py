from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, entity=None):
    url = baseUrl + "b/{bucket}/defaultObjectAcl/{entity}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, entity=None):
    url = baseUrl + "b/{bucket}/defaultObjectAcl/{entity}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(bucket=None):
    url = baseUrl + "b/{bucket}/defaultObjectAcl"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None):
    url = baseUrl + "b/{bucket}/defaultObjectAcl"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, entity=None):
    url = baseUrl + "b/{bucket}/defaultObjectAcl/{entity}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, entity=None):
    url = baseUrl + "b/{bucket}/defaultObjectAcl/{entity}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket', 'entity']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
