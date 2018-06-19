from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/annotationsets"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(annotationSetId=None):
    url = baseUrl + "v1/annotationsets/{annotationSetId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['annotationSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(annotationSetId=None):
    url = baseUrl + "v1/annotationsets/{annotationSetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['annotationSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/annotationsets/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(annotationSetId=None, updateMask=None):
    url = baseUrl + "v1/annotationsets/{annotationSetId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['annotationSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
