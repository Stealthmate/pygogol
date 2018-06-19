from pygogol.core import Request

from Defs import baseUrl

def delete(clusterId=None, enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['clusterId', 'enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(clusterId=None, enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}"
    method = "GET"
    return Request(
        method, 
        url.format(['clusterId', 'enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(clusterId=None, enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['clusterId', 'enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(clusterId=None, enterpriseId=None, pageId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout/pages/{pageId}/clusters/{clusterId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['clusterId', 'enterpriseId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
