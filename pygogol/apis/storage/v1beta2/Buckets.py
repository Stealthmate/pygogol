from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None):
    url = baseUrl + "b/{bucket}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, projection=None):
    url = baseUrl + "b"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None, project=None, projection=None):
    url = baseUrl + "b"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
