from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "webResource/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None):
    url = baseUrl + "webResource/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getToken():
    url = baseUrl + "token"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(verificationMethod=None):
    url = baseUrl + "webResource"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "webResource"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(id=None):
    url = baseUrl + "webResource/{id}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None):
    url = baseUrl + "webResource/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
