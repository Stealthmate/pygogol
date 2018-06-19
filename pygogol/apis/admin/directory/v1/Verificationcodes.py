from pygogol.core import Request

from Defs import baseUrl

def generate(userKey=None):
    url = baseUrl + "users/{userKey}/verificationCodes/generate"
    method = "POST"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def invalidate(userKey=None):
    url = baseUrl + "users/{userKey}/verificationCodes/invalidate"
    method = "POST"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(userKey=None):
    url = baseUrl + "users/{userKey}/verificationCodes"
    method = "GET"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
