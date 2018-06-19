from pygogol.core import Request

from Defs import baseUrl

def getBillingInfo(name=None):
    url = baseUrl + "v1/{+name}/billingInfo"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateBillingInfo(name=None):
    url = baseUrl + "v1/{+name}/billingInfo"
    method = "PUT"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
