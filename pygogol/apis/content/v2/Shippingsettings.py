from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "shippingsettings/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, merchantId=None):
    url = baseUrl + "{merchantId}/shippingsettings/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getsupportedcarriers(merchantId=None):
    url = baseUrl + "{merchantId}/supportedCarriers"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getsupportedholidays(merchantId=None):
    url = baseUrl + "{merchantId}/supportedHolidays"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/shippingsettings"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/shippingsettings/{accountId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/shippingsettings/{accountId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
