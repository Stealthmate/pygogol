from pygogol.core import Request

from Defs import baseUrl

def reset(eventId=None):
    url = baseUrl + "events/{eventId}/reset"
    method = "POST"
    return Request(
        method, 
        url.format(['eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAll():
    url = baseUrl + "events/reset"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetAllForAllPlayers():
    url = baseUrl + "events/resetAllForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetForAllPlayers(eventId=None):
    url = baseUrl + "events/{eventId}/resetForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format(['eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetMultipleForAllPlayers():
    url = baseUrl + "events/resetMultipleForAllPlayers"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
