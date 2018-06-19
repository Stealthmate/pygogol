from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "accounttax/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, merchantId=None):
    url = baseUrl + "{merchantId}/accounttax/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/accounttax"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/accounttax/{accountId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/accounttax/{accountId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
