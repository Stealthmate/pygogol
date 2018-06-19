from pygogol.core import Request

from Defs import baseUrl

def list(categoryId=None, forUsername=None, hl=None, id=None, managedByMe=None, maxResults=None, mine=None, mySubscribers=None, onBehalfOfContentOwner=None, pageToken=None, part=None):
    url = baseUrl + "channels"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None, part=None):
    url = baseUrl + "channels"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
