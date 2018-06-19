from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/variants"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(variantId=None):
    url = baseUrl + "v1/variants/{variantId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['variantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(variantId=None):
    url = baseUrl + "v1/variants/{variantId}"
    method = "GET"
    return Request(
        method, 
        url.format(['variantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def import():
    url = baseUrl + "v1/variants:import"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def merge():
    url = baseUrl + "v1/variants:merge"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(variantId=None, updateMask=None):
    url = baseUrl + "v1/variants/{variantId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['variantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/variants/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
