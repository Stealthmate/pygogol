from pygogol.core import Request

from Defs import baseUrl

def delete(enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
