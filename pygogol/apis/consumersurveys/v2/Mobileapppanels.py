from pygogol.core import Request

from Defs import baseUrl

def get(panelId=None):
    url = baseUrl + "mobileAppPanels/{panelId}"
    method = "GET"
    return Request(
        method, 
        url.format(['panelId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, startIndex=None, token=None):
    url = baseUrl + "mobileAppPanels"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(panelId=None):
    url = baseUrl + "mobileAppPanels/{panelId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['panelId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
