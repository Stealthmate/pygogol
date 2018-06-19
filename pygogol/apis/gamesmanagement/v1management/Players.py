from pygogol.core import Request

from Defs import baseUrl

def hide(applicationId=None, playerId=None):
    url = baseUrl + "applications/{applicationId}/players/hidden/{playerId}"
    method = "POST"
    return Request(
        method, 
        url.format(['applicationId', 'playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unhide(applicationId=None, playerId=None):
    url = baseUrl + "applications/{applicationId}/players/hidden/{playerId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['applicationId', 'playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
