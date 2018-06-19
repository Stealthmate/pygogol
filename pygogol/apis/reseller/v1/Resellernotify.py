from pygogol.core import Request

from Defs import baseUrl

def getwatchdetails():
    url = baseUrl + "resellernotify/getwatchdetails"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def register(serviceAccountEmailAddress=None):
    url = baseUrl + "resellernotify/register"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unregister(serviceAccountEmailAddress=None):
    url = baseUrl + "resellernotify/unregister"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
