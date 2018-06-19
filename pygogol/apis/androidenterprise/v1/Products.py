from pygogol.core import Request

from Defs import baseUrl

def approve(enterpriseId=None, productId=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}/approve"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generateApprovalUrl(enterpriseId=None, productId=None, languageCode=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}/generateApprovalUrl"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(enterpriseId=None, productId=None, language=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getAppRestrictionsSchema(enterpriseId=None, productId=None, language=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}/appRestrictionsSchema"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getPermissions(enterpriseId=None, productId=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}/permissions"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None, approved=None, language=None, maxResults=None, query=None, token=None):
    url = baseUrl + "enterprises/{enterpriseId}/products"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unapprove(enterpriseId=None, productId=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}/unapprove"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
