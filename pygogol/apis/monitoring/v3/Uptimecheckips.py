from pygogol.core import Request

from Defs import baseUrl

def list(pageSize=None, pageToken=None):
    url = baseUrl + "v3/uptimeCheckIps"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
