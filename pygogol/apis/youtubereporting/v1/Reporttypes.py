from pygogol.core import Request

from Defs import baseUrl

def list(includeSystemManaged=None, onBehalfOfContentOwner=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/reportTypes"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
