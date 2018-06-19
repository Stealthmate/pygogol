from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/courses"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(id=None):
    url = baseUrl + "v1/courses/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None):
    url = baseUrl + "v1/courses/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(courseStates=None, pageSize=None, pageToken=None, studentId=None, teacherId=None):
    url = baseUrl + "v1/courses"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(id=None, updateMask=None):
    url = baseUrl + "v1/courses/{id}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None):
    url = baseUrl + "v1/courses/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
