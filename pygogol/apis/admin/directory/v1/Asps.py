from pygogol.core import Request

from Defs import baseUrl

def delete(codeId=None, userKey=None):
    url = baseUrl + "users/{userKey}/asps/{codeId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['codeId', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(codeId=None, userKey=None):
    url = baseUrl + "users/{userKey}/asps/{codeId}"
    method = "GET"
    return Request(
        method, 
        url.format(['codeId', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(userKey=None):
    url = baseUrl + "users/{userKey}/asps"
    method = "GET"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
