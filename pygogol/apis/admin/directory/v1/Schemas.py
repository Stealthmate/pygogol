from pygogol.core import Request

from Defs import baseUrl

def delete(customerId=None, schemaKey=None):
    url = baseUrl + "customer/{customerId}/schemas/{schemaKey}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customerId', 'schemaKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customerId=None, schemaKey=None):
    url = baseUrl + "customer/{customerId}/schemas/{schemaKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId', 'schemaKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customerId=None):
    url = baseUrl + "customer/{customerId}/schemas"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerId=None):
    url = baseUrl + "customer/{customerId}/schemas"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customerId=None, schemaKey=None):
    url = baseUrl + "customer/{customerId}/schemas/{schemaKey}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customerId', 'schemaKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customerId=None, schemaKey=None):
    url = baseUrl + "customer/{customerId}/schemas/{schemaKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customerId', 'schemaKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
