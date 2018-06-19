from pygogol.core import Request

from Defs import baseUrl

def delete(fileId=None, propertyKey=None, visibility=None):
    url = baseUrl + "files/{fileId}/properties/{propertyKey}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['fileId', 'propertyKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(fileId=None, propertyKey=None, visibility=None):
    url = baseUrl + "files/{fileId}/properties/{propertyKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId', 'propertyKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(fileId=None):
    url = baseUrl + "files/{fileId}/properties"
    method = "POST"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(fileId=None):
    url = baseUrl + "files/{fileId}/properties"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(fileId=None, propertyKey=None, visibility=None):
    url = baseUrl + "files/{fileId}/properties/{propertyKey}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['fileId', 'propertyKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(fileId=None, propertyKey=None, visibility=None):
    url = baseUrl + "files/{fileId}/properties/{propertyKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['fileId', 'propertyKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
