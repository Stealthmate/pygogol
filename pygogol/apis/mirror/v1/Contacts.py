from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "contacts/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None):
    url = baseUrl + "contacts/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "contacts"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "contacts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(id=None):
    url = baseUrl + "contacts/{id}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None):
    url = baseUrl + "contacts/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
