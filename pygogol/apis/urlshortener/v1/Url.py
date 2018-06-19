from pygogol.core import Request

from Defs import baseUrl

def get(projection=None, shortUrl=None):
    url = baseUrl + "url"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "url"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(projection=None, start-token=None):
    url = baseUrl + "url/history"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
