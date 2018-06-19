from pygogol.core import Request

from Defs import baseUrl

def delete(clientId=None, userKey=None):
    url = baseUrl + "users/{userKey}/tokens/{clientId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['clientId', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(clientId=None, userKey=None):
    url = baseUrl + "users/{userKey}/tokens/{clientId}"
    method = "GET"
    return Request(
        method, 
        url.format(['clientId', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(userKey=None):
    url = baseUrl + "users/{userKey}/tokens"
    method = "GET"
    return Request(
        method, 
        url.format(['userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
