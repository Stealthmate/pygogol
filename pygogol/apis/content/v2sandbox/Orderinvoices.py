from pygogol.core import Request

from Defs import baseUrl

def createchargeinvoice(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orderinvoices/{orderId}/createChargeInvoice"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def createrefundinvoice(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orderinvoices/{orderId}/createRefundInvoice"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
