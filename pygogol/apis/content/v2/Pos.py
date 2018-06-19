from pygogol.core import Request

from Defs import baseUrl

def custombatch(dryRun=None):
    url = baseUrl + "pos/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(merchantId=None, storeCode=None, targetMerchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/pos/{targetMerchantId}/store/{storeCode}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['merchantId', 'storeCode', 'targetMerchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(merchantId=None, storeCode=None, targetMerchantId=None):
    url = baseUrl + "{merchantId}/pos/{targetMerchantId}/store/{storeCode}"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'storeCode', 'targetMerchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(merchantId=None, targetMerchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/pos/{targetMerchantId}/store"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'targetMerchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def inventory(merchantId=None, targetMerchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/pos/{targetMerchantId}/inventory"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'targetMerchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, targetMerchantId=None):
    url = baseUrl + "{merchantId}/pos/{targetMerchantId}/store"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'targetMerchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def sale(merchantId=None, targetMerchantId=None, dryRun=None):
    url = baseUrl + "{merchantId}/pos/{targetMerchantId}/sale"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'targetMerchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
