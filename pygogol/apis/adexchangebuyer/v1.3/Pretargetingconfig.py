from pygogol.core import Request

from Defs import baseUrl

def delete(accountId=None, configId=None):
    url = baseUrl + "pretargetingconfigs/{accountId}/{configId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['accountId', 'configId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(accountId=None, configId=None):
    url = baseUrl + "pretargetingconfigs/{accountId}/{configId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'configId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(accountId=None):
    url = baseUrl + "pretargetingconfigs/{accountId}"
    method = "POST"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(accountId=None):
    url = baseUrl + "pretargetingconfigs/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(accountId=None, configId=None):
    url = baseUrl + "pretargetingconfigs/{accountId}/{configId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['accountId', 'configId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, configId=None):
    url = baseUrl + "pretargetingconfigs/{accountId}/{configId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId', 'configId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
