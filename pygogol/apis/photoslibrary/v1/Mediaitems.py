from pygogol.core import Request

from Defs import baseUrl

def batchCreate():
    url = baseUrl + "v1/mediaItems:batchCreate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(mediaItemId=None):
    url = baseUrl + "v1/mediaItems/{+mediaItemId}"
    method = "GET"
    return Request(
        method, 
        url.format(['mediaItemId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/mediaItems:search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
