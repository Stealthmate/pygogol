from pygogol.core import Request

from Defs import baseUrl

def get(userId=None):
    url = baseUrl + "users/{userId}"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
