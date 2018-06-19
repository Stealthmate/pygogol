from pygogol.core import Request

from Defs import baseUrl

def get(userId=None):
    url = baseUrl + "v1/userProfiles/{userId}"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
