from pygogol.core import Request

from Defs import baseUrl

def listByPlayer(language=None, maxResults=None, pageToken=None):
    url = baseUrl + "events"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listDefinitions(language=None, maxResults=None, pageToken=None):
    url = baseUrl + "eventDefinitions"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def record(language=None):
    url = baseUrl + "events"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
