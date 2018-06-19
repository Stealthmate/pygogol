from pygogol.core import Request

from Defs import baseUrl

def list(adClientId=None, maxResults=None, pageToken=None):
    url = baseUrl + "adclients/{adClientId}/urlchannels"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
