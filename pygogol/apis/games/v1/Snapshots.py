from pygogol.core import Request

from Defs import baseUrl

def get(snapshotId=None, language=None):
    url = baseUrl + "snapshots/{snapshotId}"
    method = "GET"
    return Request(
        method, 
        url.format(['snapshotId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(playerId=None, language=None, maxResults=None, pageToken=None):
    url = baseUrl + "players/{playerId}/snapshots"
    method = "GET"
    return Request(
        method, 
        url.format(['playerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
