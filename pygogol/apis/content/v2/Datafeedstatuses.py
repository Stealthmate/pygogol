from pygogol.core import Request

from Defs import baseUrl

def custombatch():
    url = baseUrl + "datafeedstatuses/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(datafeedId=None, merchantId=None, country=None, language=None):
    url = baseUrl + "{merchantId}/datafeedstatuses/{datafeedId}"
    method = "GET"
    return Request(
        method, 
        url.format(['datafeedId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/datafeedstatuses"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
