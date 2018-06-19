from pygogol.core import Request

from Defs import baseUrl

def notifyauthapproved(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orderpayments/{orderId}/notifyAuthApproved"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def notifyauthdeclined(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orderpayments/{orderId}/notifyAuthDeclined"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def notifycharge(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orderpayments/{orderId}/notifyCharge"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def notifyrefund(merchantId=None, orderId=None):
    url = baseUrl + "{merchantId}/orderpayments/{orderId}/notifyRefund"
    method = "POST"
    return Request(
        method, 
        url.format(['merchantId', 'orderId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
