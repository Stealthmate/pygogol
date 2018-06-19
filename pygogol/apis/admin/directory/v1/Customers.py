from pygogol.core import Request

from Defs import baseUrl

def get(customerKey=None):
    url = baseUrl + "customers/{customerKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customerKey=None):
    url = baseUrl + "customers/{customerKey}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customerKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customerKey=None):
    url = baseUrl + "customers/{customerKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customerKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
