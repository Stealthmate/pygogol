from pygogol.core import Request

from Defs import baseUrl

def generate(dimension=None, endDate=None, filter=None, locale=None, maxResults=None, metric=None, sort=None, startDate=None, startIndex=None):
    url = baseUrl + "reports"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
