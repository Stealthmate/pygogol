from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, object=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, object=None, projection=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(bucket=None, name=None, projection=None):
    url = baseUrl + "b/{bucket}/o"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bucket=None, delimiter=None, max-results=None, pageToken=None, prefix=None, projection=None):
    url = baseUrl + "b/{bucket}/o"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, object=None, projection=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, object=None, projection=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
