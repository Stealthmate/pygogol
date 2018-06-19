from pygogol.core import Request

from Defs import baseUrl

def create(callbackUrl=None, projectId=None):
    url = baseUrl + "v1/signupUrls"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
