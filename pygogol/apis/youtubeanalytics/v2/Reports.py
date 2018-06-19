from pygogol.core import Request

from Defs import baseUrl

def query(currency=None, dimensions=None, endDate=None, filters=None, ids=None, includeHistoricalChannelData=None, maxResults=None, metrics=None, sort=None, startDate=None, startIndex=None):
    url = baseUrl + "v2/reports"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
