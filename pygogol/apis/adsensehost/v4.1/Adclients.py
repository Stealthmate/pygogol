from pygogol.core import Request

from Defs import baseUrl

def get(adClientId=None):
    url = baseUrl + "adclients/{adClientId}"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None):
    url = baseUrl + "adclients"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
