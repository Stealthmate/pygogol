from pygogol.core import Request

from Defs import baseUrl

def list(accountId=None, endDateTime=None, maxResults=None, pageToken=None, startDateTime=None):
    url = baseUrl + "performancereport"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
