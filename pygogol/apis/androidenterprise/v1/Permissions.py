from pygogol.core import Request

from Defs import baseUrl

def get(permissionId=None, language=None):
    url = baseUrl + "permissions/{permissionId}"
    method = "GET"
    return Request(
        method, 
        url.format(['permissionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
