from pygogol.core import Request

from Defs import baseUrl

def accept(id=None):
    url = baseUrl + "v1/invitations/{id}:accept"
    method = "POST"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/invitations"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(id=None):
    url = baseUrl + "v1/invitations/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None):
    url = baseUrl + "v1/invitations/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(courseId=None, pageSize=None, pageToken=None, userId=None):
    url = baseUrl + "v1/invitations"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
