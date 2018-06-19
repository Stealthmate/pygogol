from pygogol.core import Request

from Defs import baseUrl

def delete(data=None):
    url = baseUrl + "training/{data}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['data']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(data=None):
    url = baseUrl + "training/{data}"
    method = "GET"
    return Request(
        method, 
        url.format(['data']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(data=None):
    url = baseUrl + "training"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(data=None):
    url = baseUrl + "training/{data}"
    method = "PUT"
    return Request(
        method, 
        url.format(['data']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
