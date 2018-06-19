from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None):
    url = baseUrl + "b/{bucket}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(projection=None):
    url = baseUrl + "b"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(max-results=None, pageToken=None, projectId=None, projection=None):
    url = baseUrl + "b"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
