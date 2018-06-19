from pygogol.core import Request

from Defs import baseUrl

def increment(achievementId=None, requestId=None, stepsToIncrement=None):
    url = baseUrl + "achievements/{achievementId}/increment"
    method = "POST"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(playerId=None, language=None, maxResults=None, pageToken=None, state=None):
    url = baseUrl + "players/{playerId}/achievements"
    method = "GET"
    return Request(
        method, 
        url.format(['playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reveal(achievementId=None):
    url = baseUrl + "achievements/{achievementId}/reveal"
    method = "POST"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setStepsAtLeast(achievementId=None, steps=None):
    url = baseUrl + "achievements/{achievementId}/setStepsAtLeast"
    method = "POST"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unlock(achievementId=None):
    url = baseUrl + "achievements/{achievementId}/unlock"
    method = "POST"
    return Request(
        method, 
        url.format(['achievementId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateMultiple():
    url = baseUrl + "achievements/updateMultiple"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
