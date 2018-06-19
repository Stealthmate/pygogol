from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, type=None):
    url = baseUrl + "{project}/global/types/{type}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'type']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, type=None):
    url = baseUrl + "{project}/global/types/{type}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'type']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "{project}/global/types"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/types"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, type=None):
    url = baseUrl + "{project}/global/types/{type}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'type']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, type=None):
    url = baseUrl + "{project}/global/types/{type}"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'type']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
