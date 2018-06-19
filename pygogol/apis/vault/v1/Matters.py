from pygogol.core import Request

from Defs import baseUrl

def addPermissions(matterId=None):
    url = baseUrl + "v1/matters/{matterId}:addPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def close(matterId=None):
    url = baseUrl + "v1/matters/{matterId}:close"
    method = "POST"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/matters"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(matterId=None):
    url = baseUrl + "v1/matters/{matterId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(matterId=None, view=None):
    url = baseUrl + "v1/matters/{matterId}"
    method = "GET"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None, state=None, view=None):
    url = baseUrl + "v1/matters"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removePermissions(matterId=None):
    url = baseUrl + "v1/matters/{matterId}:removePermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reopen(matterId=None):
    url = baseUrl + "v1/matters/{matterId}:reopen"
    method = "POST"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def undelete(matterId=None):
    url = baseUrl + "v1/matters/{matterId}:undelete"
    method = "POST"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(matterId=None):
    url = baseUrl + "v1/matters/{matterId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['matterId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
