from pygogol.core import Request

from Defs import baseUrl

def delete(adClientId=None, customChannelId=None):
    url = baseUrl + "adclients/{adClientId}/customchannels/{customChannelId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['adClientId', 'customChannelId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(adClientId=None, customChannelId=None):
    url = baseUrl + "adclients/{adClientId}/customchannels/{customChannelId}"
    method = "GET"
    return Request(
        method, 
        url.format(['adClientId', 'customChannelId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(adClientId=None):
    url = baseUrl + "adclients/{adClientId}/customchannels"
    method = "POST"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
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

def patch(adClientId=None, customChannelId=None):
    url = baseUrl + "adclients/{adClientId}/customchannels"
    method = "PATCH"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(adClientId=None):
    url = baseUrl + "adclients/{adClientId}/customchannels"
    method = "PUT"
    return Request(
        method, 
        url.format(['adClientId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
