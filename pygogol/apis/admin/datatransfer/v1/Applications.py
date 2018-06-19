from pygogol.core import Request

from Defs import baseUrl

def get(applicationId=None):
    url = baseUrl + "applications/{applicationId}"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerId=None, maxResults=None, pageToken=None):
    url = baseUrl + "applications"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
