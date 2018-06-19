from pygogol.core import Request

from Defs import baseUrl

def join():
    url = baseUrl + "v1/sharedAlbums:join"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None):
    url = baseUrl + "v1/sharedAlbums"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
