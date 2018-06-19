from pygogol.core import Request

from Defs import baseUrl

def get(adClientId=None, customChannelId=None):
    url = baseUrl + "adclients/{adClientId}/customchannels/{customChannelId}"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId', 'customChannelId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(adClientId=None, maxResults=None, pageToken=None):
    url = baseUrl + "adclients/{adClientId}/customchannels"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
