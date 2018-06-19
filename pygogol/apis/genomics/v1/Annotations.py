from pygogol.core import Request

from Defs import baseUrl

def batchCreate():
    url = baseUrl + "v1/annotations:batchCreate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/annotations"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(annotationId=None):
    url = baseUrl + "v1/annotations/{annotationId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['annotationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(annotationId=None):
    url = baseUrl + "v1/annotations/{annotationId}"
    method = "GET"
    return Request(
        method, 
        url.format(['annotationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/annotations/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(annotationId=None, updateMask=None):
    url = baseUrl + "v1/annotations/{annotationId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['annotationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
