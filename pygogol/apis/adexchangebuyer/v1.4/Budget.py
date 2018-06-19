from pygogol.core import Request

from Defs import baseUrl

def get(accountId=None, billingId=None):
    url = baseUrl + "billinginfo/{accountId}/{billingId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId', 'billingId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(accountId=None, billingId=None):
    url = baseUrl + "billinginfo/{accountId}/{billingId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['accountId', 'billingId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(accountId=None, billingId=None):
    url = baseUrl + "billinginfo/{accountId}/{billingId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['accountId', 'billingId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
