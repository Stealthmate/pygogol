from pygogol.core import Request

from Defs import baseUrl

def get(groupUniqueId=None):
    url = baseUrl + "{groupUniqueId}"
    method = "GET"
    return Request(
        method, 
        url.format(['groupUniqueId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(groupUniqueId=None):
    url = baseUrl + "{groupUniqueId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['groupUniqueId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(groupUniqueId=None):
    url = baseUrl + "{groupUniqueId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['groupUniqueId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
