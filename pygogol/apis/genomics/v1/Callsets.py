from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/callsets"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(callSetId=None):
    url = baseUrl + "v1/callsets/{callSetId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['callSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(callSetId=None):
    url = baseUrl + "v1/callsets/{callSetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['callSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(callSetId=None, updateMask=None):
    url = baseUrl + "v1/callsets/{callSetId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['callSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/callsets/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
