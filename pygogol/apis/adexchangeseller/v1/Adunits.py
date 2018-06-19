from pygogol.core import Request

from Defs import baseUrl

def get(adClientId=None, adUnitId=None):
    url = baseUrl + "adclients/{adClientId}/adunits/{adUnitId}"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId', 'adUnitId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(adClientId=None, includeInactive=None, maxResults=None, pageToken=None):
    url = baseUrl + "adclients/{adClientId}/adunits"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
