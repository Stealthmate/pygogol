from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "liasettings/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, merchantId=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getaccessiblegmbaccounts(accountId=None, merchantId=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}/accessiblegmbaccounts"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{merchantId}/liasettings"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listposdataproviders():
    url = baseUrl + "liasettings/posdataproviders"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def requestgmbaccess(accountId=None, merchantId=None, gmbEmail=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}/requestgmbaccess"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def requestinventoryverification(accountId=None, country=None, merchantId=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}/requestinventoryverification/{country}"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'country', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setinventoryverificationcontact(accountId=None, merchantId=None, contactEmail=None, contactName=None, country=None, language=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}/setinventoryverificationcontact"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setposdataprovider(accountId=None, merchantId=None, country=None, posDataProviderId=None, posExternalAccountId=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}/setposdataprovider"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, merchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/liasettings/{accountId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId', 'merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
