from pygogol.core import Request

from Defs import baseUrl

def get(summaryId=None, volumeId=None, contentVersion=None, source=None):
    url = baseUrl + "volumes/{volumeId}/layersummary/{summaryId}"
    method = "GET"
    return Request(
        method, 
        url.format(['summaryId', 'volumeId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(volumeId=None, contentVersion=None, maxResults=None, pageToken=None, source=None):
    url = baseUrl + "volumes/{volumeId}/layersummary"
    method = "GET"
    return Request(
        method, 
        url.format(['volumeId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
