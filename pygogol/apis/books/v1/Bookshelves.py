from pygogol.core import Request

from Defs import baseUrl

def get(shelf=None, userId=None, source=None):
    url = baseUrl + "users/{userId}/bookshelves/{shelf}"
    method = "GET"
    return Request(
        method, 
        url.format(['shelf', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(userId=None, source=None):
    url = baseUrl + "users/{userId}/bookshelves"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
