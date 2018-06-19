from pygogol.core import Request

from Defs import baseUrl

def get(bucket=None, ifMetagenerationMatch=None, projection=None):
    url = baseUrl + "b/{bucket}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
