from pygogol.core import Request

from Defs import baseUrl

def insert(groupId=None):
    url = baseUrl + "{groupId}/archive"
    method = "POST"
    return Request(
        method, 
        url.format(['groupId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
