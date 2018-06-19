from pygogol.core import Request

from Defs import baseUrl

def query(currency=None, dimensions=None, end-date=None, filters=None, ids=None, include-historical-channel-data=None, max-results=None, metrics=None, sort=None, start-date=None, start-index=None):
    url = baseUrl + "reports"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
