from pygogol.core import Request

from Defs import baseUrl

def start(productCode=None, userLocale=None, websiteLocale=None, websiteUrl=None):
    url = baseUrl + "associationsessions/start"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verify(token=None):
    url = baseUrl + "associationsessions/verify"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
