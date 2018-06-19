from pygogol.core import Request

from Defs import baseUrl

def delete(packageName=None, sku=None):
    url = baseUrl + "{packageName}/inappproducts/{sku}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['packageName', 'sku']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(packageName=None, sku=None):
    url = baseUrl + "{packageName}/inappproducts/{sku}"
    method = "GET"
    return Request(
        method, 
        url.format(['packageName', 'sku']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(packageName=None, autoConvertMissingPrices=None):
    url = baseUrl + "{packageName}/inappproducts"
    method = "POST"
    return Request(
        method, 
        url.format(['packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(packageName=None, maxResults=None, startIndex=None, token=None):
    url = baseUrl + "{packageName}/inappproducts"
    method = "GET"
    return Request(
        method, 
        url.format(['packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(packageName=None, sku=None, autoConvertMissingPrices=None):
    url = baseUrl + "{packageName}/inappproducts/{sku}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['packageName', 'sku']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(packageName=None, sku=None, autoConvertMissingPrices=None):
    url = baseUrl + "{packageName}/inappproducts/{sku}"
    method = "PUT"
    return Request(
        method, 
        url.format(['packageName', 'sku']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
