from pygogol.core import Request

from Defs import baseUrl

def get(fileId=None, revision=None):
    url = baseUrl + "files/{fileId}/realtime"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(fileId=None, baseRevision=None):
    url = baseUrl + "files/{fileId}/realtime"
    method = "PUT"
    return Request(
        method, 
        url.format(['fileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
