from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "inventory/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def set(merchantId=None, productId=None, storeCode=None, dryRun=None):
    url = baseUrl + "{merchantId}/inventory/{storeCode}/products/{productId}"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'productId', 'storeCode']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
