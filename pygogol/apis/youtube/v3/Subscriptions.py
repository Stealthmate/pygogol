from pygogol.core import Request

from Defs import baseUrl

def delete(id=None):
    url = baseUrl + "subscriptions"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(part=None):
    url = baseUrl + "subscriptions"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(channelId=None, forChannelId=None, id=None, maxResults=None, mine=None, myRecentSubscribers=None, mySubscribers=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, order=None, pageToken=None, part=None):
    url = baseUrl + "subscriptions"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
