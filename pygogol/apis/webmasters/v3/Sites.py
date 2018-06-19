from pygogol.core import Request

from Defs import baseUrl

def add(siteUrl=None):
    url = baseUrl + "sites/{siteUrl}"
    method = "PUT"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(siteUrl=None):
    url = baseUrl + "sites/{siteUrl}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(siteUrl=None):
    url = baseUrl + "sites/{siteUrl}"
    method = "GET"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "sites"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
