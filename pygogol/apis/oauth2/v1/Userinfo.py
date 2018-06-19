from pygogol.core import Request

from Defs import baseUrl

def get():
    url = baseUrl + "oauth2/v1/userinfo"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
