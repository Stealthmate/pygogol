from pygogol.core import Request

from Defs import baseUrl

def get(date=None, customerId=None, pageToken=None, parameters=None):
    url = baseUrl + "usage/dates/{date}"
    method = "GET"
    return Request(
        method, 
        url.format(['date']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
