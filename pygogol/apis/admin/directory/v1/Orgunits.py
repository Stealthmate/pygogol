from pygogol.core import Request

from Defs import baseUrl

def delete(customerId=None, orgUnitPath=None):
    url = baseUrl + "customer/{customerId}/orgunits{/orgUnitPath*}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customerId', 'orgUnitPath']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customerId=None, orgUnitPath=None):
    url = baseUrl + "customer/{customerId}/orgunits{/orgUnitPath*}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId', 'orgUnitPath']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customerId=None):
    url = baseUrl + "customer/{customerId}/orgunits"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerId=None, orgUnitPath=None, type=None):
    url = baseUrl + "customer/{customerId}/orgunits"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customerId=None, orgUnitPath=None):
    url = baseUrl + "customer/{customerId}/orgunits{/orgUnitPath*}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customerId', 'orgUnitPath']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customerId=None, orgUnitPath=None):
    url = baseUrl + "customer/{customerId}/orgunits{/orgUnitPath*}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customerId', 'orgUnitPath']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
