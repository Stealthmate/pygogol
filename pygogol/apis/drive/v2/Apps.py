from pygogol.core import Request

from Defs import baseUrl

def get(appId=None):
    url = baseUrl + "apps/{appId}"
    method = "GET"
    return Request(
        method, 
        url.format(['appId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(appFilterExtensions=None, appFilterMimeTypes=None, languageCode=None):
    url = baseUrl + "apps"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
