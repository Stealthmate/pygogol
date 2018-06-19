from pygogol.core import Request

from Defs import baseUrl

def get(applicationId=None, language=None, platformType=None):
    url = baseUrl + "applications/{applicationId}"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def played():
    url = baseUrl + "applications/played"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verify(applicationId=None):
    url = baseUrl + "applications/{applicationId}/verify"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
