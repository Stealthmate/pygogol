from pygogol.core import Request

from Defs import baseUrl

def delete(adClientId=None, urlChannelId=None):
    url = baseUrl + "adclients/{adClientId}/urlchannels/{urlChannelId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['adClientId', 'urlChannelId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(adClientId=None):
    url = baseUrl + "adclients/{adClientId}/urlchannels"
    method = "POST"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(adClientId=None, maxResults=None, pageToken=None):
    url = baseUrl + "adclients/{adClientId}/urlchannels"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
