from pygogol.core import Request

from Defs import baseUrl

def delete(productId=None, skuId=None, userId=None):
    url = baseUrl + "{productId}/sku/{skuId}/user/{userId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['productId', 'skuId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(productId=None, skuId=None, userId=None):
    url = baseUrl + "{productId}/sku/{skuId}/user/{userId}"
    method = "GET"
    return Request(
        method, 
        url.format(['productId', 'skuId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(productId=None, skuId=None):
    url = baseUrl + "{productId}/sku/{skuId}/user"
    method = "POST"
    return Request(
        method, 
        url.format(['productId', 'skuId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listForProduct(productId=None, customerId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{productId}/users"
    method = "GET"
    return Request(
        method, 
        url.format(['productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listForProductAndSku(productId=None, skuId=None, customerId=None, maxResults=None, pageToken=None):
    url = baseUrl + "{productId}/sku/{skuId}/users"
    method = "GET"
    return Request(
        method, 
        url.format(['productId', 'skuId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(productId=None, skuId=None, userId=None):
    url = baseUrl + "{productId}/sku/{skuId}/user/{userId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['productId', 'skuId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(productId=None, skuId=None, userId=None):
    url = baseUrl + "{productId}/sku/{skuId}/user/{userId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['productId', 'skuId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
