from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, onBehalfOfContentOwner=None):
    url = baseUrl + "videos"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getRating(id=None, onBehalfOfContentOwner=None):
    url = baseUrl + "videos/getRating"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(autoLevels=None, notifySubscribers=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None, stabilize=None):
    url = baseUrl + "videos"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(chart=None, hl=None, id=None, locale=None, maxHeight=None, maxResults=None, maxWidth=None, myRating=None, onBehalfOfContentOwner=None, pageToken=None, part=None, regionCode=None, videoCategoryId=None):
    url = baseUrl + "videos"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rate(id=None, rating=None):
    url = baseUrl + "videos/rate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reportAbuse(onBehalfOfContentOwner=None):
    url = baseUrl + "videos/reportAbuse"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None, part=None):
    url = baseUrl + "videos"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
