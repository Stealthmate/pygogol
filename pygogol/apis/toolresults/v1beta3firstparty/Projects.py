from pygogol.core import Request

from Defs import baseUrl

def getSettings(projectId=None):
    url = baseUrl + "{projectId}/settings"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def initializeSettings(projectId=None):
    url = baseUrl + "{projectId}:initializeSettings"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
