from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/photo"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(photoId=None):
    url = baseUrl + "v1/photo/{photoId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['photoId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(photoId=None, view=None):
    url = baseUrl + "v1/photo/{photoId}"
    method = "GET"
    return Request(
        method, 
        url.format(['photoId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def startUpload():
    url = baseUrl + "v1/photo:startUpload"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None, updateMask=None):
    url = baseUrl + "v1/photo/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
