from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "datafeeds/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(datafeedId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/datafeeds/{datafeedId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['datafeedId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def fetchnow(datafeedId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/datafeeds/{datafeedId}/fetchNow"
    method = "POST"
    return Request(
        method, 
        url.format(['datafeedId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(datafeedId=None, merchantId=None):
    url = baseUrl + "{merchantId}/datafeeds/{datafeedId}"
    method = "GET"
    return Request(
        method, 
        url.format(['datafeedId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/datafeeds"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/datafeeds"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(datafeedId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/datafeeds/{datafeedId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['datafeedId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(datafeedId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/datafeeds/{datafeedId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['datafeedId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
