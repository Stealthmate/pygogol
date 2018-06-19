from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/variantsets"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(variantSetId=None):
    url = baseUrl + "v1/variantsets/{variantSetId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['variantSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def export(variantSetId=None):
    url = baseUrl + "v1/variantsets/{variantSetId}:export"
    method = "POST"
    return Request(
        method, 
        url.format(['variantSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(variantSetId=None):
    url = baseUrl + "v1/variantsets/{variantSetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['variantSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(variantSetId=None, updateMask=None):
    url = baseUrl + "v1/variantsets/{variantSetId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['variantSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/variantsets/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
