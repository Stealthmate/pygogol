from pygogol.core import Request

from Defs import baseUrl

def bind(id=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None, streamId=None):
    url = baseUrl + "liveBroadcasts/bind"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def control(displaySlate=None, id=None, offsetTimeMs=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None, walltime=None):
    url = baseUrl + "liveBroadcasts/control"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(id=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None):
    url = baseUrl + "liveBroadcasts"
    method = "DELETE"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None):
    url = baseUrl + "liveBroadcasts"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(broadcastStatus=None, broadcastType=None, id=None, maxResults=None, mine=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, pageToken=None, part=None):
    url = baseUrl + "liveBroadcasts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def transition(broadcastStatus=None, id=None, onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None):
    url = baseUrl + "liveBroadcasts/transition"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(onBehalfOfContentOwner=None, onBehalfOfContentOwnerChannel=None, part=None):
    url = baseUrl + "liveBroadcasts"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
