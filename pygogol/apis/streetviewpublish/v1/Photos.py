from pygogol.core import Request

from Defs import baseUrl

def batchDelete():
    url = baseUrl + "v1/photos:batchDelete"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def batchGet(photoIds=None, view=None):
    url = baseUrl + "v1/photos:batchGet"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def batchUpdate():
    url = baseUrl + "v1/photos:batchUpdate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, pageSize=None, pageToken=None, view=None):
    url = baseUrl + "v1/photos"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
