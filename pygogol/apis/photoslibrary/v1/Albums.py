from pygogol.core import Request

from Defs import baseUrl

def addEnrichment(albumId=None):
    url = baseUrl + "v1/albums/{+albumId}:addEnrichment"
    method = "POST"
    return Request(
        method, 
        url.format(['albumId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/albums"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(albumId=None):
    url = baseUrl + "v1/albums/{+albumId}"
    method = "GET"
    return Request(
        method, 
        url.format(['albumId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None):
    url = baseUrl + "v1/albums"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def share(albumId=None):
    url = baseUrl + "v1/albums/{+albumId}:share"
    method = "POST"
    return Request(
        method, 
        url.format(['albumId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
