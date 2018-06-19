from pygogol.core import Request

from Defs import baseUrl

def get(includeSubscribed=None, maxChangeIdCount=None, startChangeId=None):
    url = baseUrl + "about"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
