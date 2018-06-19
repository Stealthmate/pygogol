from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1beta1a/topics"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(topic=None):
    url = baseUrl + "v1beta1a/topics/{+topic}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['topic']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(topic=None):
    url = baseUrl + "v1beta1a/topics/{+topic}"
    method = "GET"
    return Request(
        method, 
        url.format(['topic']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None, query=None):
    url = baseUrl + "v1beta1a/topics"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def publish():
    url = baseUrl + "v1beta1a/topics/publish"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def publishBatch():
    url = baseUrl + "v1beta1a/topics/publishBatch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
