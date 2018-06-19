from pygogol.core import Request

from Defs import baseUrl

def getProfile(userId=None):
    url = baseUrl + "{userId}/profile"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def stop(userId=None):
    url = baseUrl + "{userId}/stop"
    method = "POST"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(userId=None):
    url = baseUrl + "{userId}/watch"
    method = "POST"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
