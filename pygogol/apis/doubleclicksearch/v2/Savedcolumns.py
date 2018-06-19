from pygogol.core import Request

from Defs import baseUrl

def list(advertiserId=None, agencyId=None):
    url = baseUrl + "agency/{agencyId}/advertiser/{advertiserId}/savedcolumns"
    method = "GET"
    return Request(
        method, 
        url.format(['advertiserId', 'agencyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
