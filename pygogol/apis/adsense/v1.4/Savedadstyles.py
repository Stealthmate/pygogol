from pygogol.core import Request

from Defs import baseUrl

def get(savedAdStyleId=None):
    url = baseUrl + "savedadstyles/{savedAdStyleId}"
    method = "GET"
    return Request(
        method, 
        url.format(['savedAdStyleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None):
    url = baseUrl + "savedadstyles"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
