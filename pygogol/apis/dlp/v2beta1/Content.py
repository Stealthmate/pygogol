from pygogol.core import Request

from Defs import baseUrl

def deidentify():
    url = baseUrl + "v2beta1/content:deidentify"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def inspect():
    url = baseUrl + "v2beta1/content:inspect"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def redact():
    url = baseUrl + "v2beta1/content:redact"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
