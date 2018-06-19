from pygogol.core import Request

from Defs import baseUrl

def get(dealId=None):
    url = baseUrl + "preferreddeals/{dealId}"
    method = "GET"
    return Request(
        method, 
        url.format(['dealId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list():
    url = baseUrl + "preferreddeals"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
