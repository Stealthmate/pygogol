from pygogol.core import Request

from Defs import baseUrl

def batchUpdate(presentationId=None):
    url = baseUrl + "v1/presentations/{presentationId}:batchUpdate"
    method = "POST"
    return Request(
        method, 
        url.format(['presentationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/presentations"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(presentationId=None):
    url = baseUrl + "v1/presentations/{+presentationId}"
    method = "GET"
    return Request(
        method, 
        url.format(['presentationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
