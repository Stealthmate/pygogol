from pygogol.core import Request

from Defs import baseUrl

def create(language=None):
    url = baseUrl + "rooms/create"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def decline(roomId=None, language=None):
    url = baseUrl + "rooms/{roomId}/decline"
    method = "POST"
    return Request(
        method, 
        url.format(['roomId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def dismiss(roomId=None):
    url = baseUrl + "rooms/{roomId}/dismiss"
    method = "POST"
    return Request(
        method, 
        url.format(['roomId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(roomId=None, language=None):
    url = baseUrl + "rooms/{roomId}"
    method = "GET"
    return Request(
        method, 
        url.format(['roomId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def join(roomId=None, language=None):
    url = baseUrl + "rooms/{roomId}/join"
    method = "POST"
    return Request(
        method, 
        url.format(['roomId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def leave(roomId=None, language=None):
    url = baseUrl + "rooms/{roomId}/leave"
    method = "POST"
    return Request(
        method, 
        url.format(['roomId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(language=None, maxResults=None, pageToken=None):
    url = baseUrl + "rooms"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reportStatus(roomId=None, language=None):
    url = baseUrl + "rooms/{roomId}/reportstatus"
    method = "POST"
    return Request(
        method, 
        url.format(['roomId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
