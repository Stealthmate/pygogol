from pygogol.core import Request

from Defs import baseUrl

def acknowledge(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/acknowledge"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def advancetestorder(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/testorders/{orderId}/advance"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def cancel(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/cancel"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def cancellineitem(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/cancelLineItem"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def createtestorder(merchantId=None):
    url = baseUrl + "{merchantId}/testorders"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def custombatch():
    url = baseUrl + "orders/batch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getbymerchantorderid(merchantId=None, merchantOrderId=None):
    url = baseUrl + "{merchantId}/ordersbymerchantid/{merchantOrderId}"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'merchantOrderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def gettestordertemplate(merchantId=None, templateName=None):
    url = baseUrl + "{merchantId}/testordertemplates/{templateName}"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId', 'templateName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def instorerefundlineitem(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/inStoreRefundLineItem"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(merchantId=None, acknowledged=None, maxResults=None, orderBy=None, pageToken=None, placedDateEnd=None, placedDateStart=None, statuses=None):
    url = baseUrl + "{merchantId}/orders"
    method = "GET"
    return Request(
        method, 
        url.format(['merchantId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def refund(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/refund"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rejectreturnlineitem(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/rejectReturnLineItem"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def returnlineitem(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/returnLineItem"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def returnrefundlineitem(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/returnRefundLineItem"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setlineitemmetadata(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/setLineItemMetadata"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def shiplineitems(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/shipLineItems"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updatelineitemshippingdetails(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/updateLineItemShippingDetails"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updatemerchantorderid(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/updateMerchantOrderId"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateshipment(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orders/{orderId}/updateShipment"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
