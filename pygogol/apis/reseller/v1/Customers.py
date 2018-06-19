from pygogol.core import Request

from Defs import baseUrl

def get(customerId=None):
    url = baseUrl + "customers/{customerId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customerAuthToken=None):
    url = baseUrl + "customers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customerId=None):
    url = baseUrl + "customers/{customerId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customerId=None):
    url = baseUrl + "customers/{customerId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
