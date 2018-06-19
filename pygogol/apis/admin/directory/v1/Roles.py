from pygogol.core import Request

from Defs import baseUrl

def delete(customer=None, roleId=None):
    url = baseUrl + "customer/{customer}/roles/{roleId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customer', 'roleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customer=None, roleId=None):
    url = baseUrl + "customer/{customer}/roles/{roleId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customer', 'roleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customer=None):
    url = baseUrl + "customer/{customer}/roles"
    method = "POST"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customer=None, maxResults=None, pageToken=None):
    url = baseUrl + "customer/{customer}/roles"
    method = "GET"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customer=None, roleId=None):
    url = baseUrl + "customer/{customer}/roles/{roleId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customer', 'roleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customer=None, roleId=None):
    url = baseUrl + "customer/{customer}/roles/{roleId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customer', 'roleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
