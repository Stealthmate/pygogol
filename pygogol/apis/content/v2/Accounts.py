from pygogol.core import Request

from Defs import baseUrl

def authinfo():
    url = baseUrl + "accounts/authinfo"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def claimwebsite(accountId=None, merchantId=None, overwrite=None):
    url = baseUrl + "{merchantId}/accounts/{accountId}/claimwebsite"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def custombatch(dryRun=None):
    url = baseUrl + "accounts/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(accountId=None, merchantId=None, dryRun=None, force=None):
    url = baseUrl + "{merchantId}/accounts/{accountId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, merchantId=None):
    url = baseUrl + "{merchantId}/accounts/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/accounts"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/accounts"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/accounts/{accountId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/accounts/{accountId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
