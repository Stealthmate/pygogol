from pygogol.core import Request

from Defs import baseUrl

def delete(customer=None, domainName=None):
    url = baseUrl + "customer/{customer}/domains/{domainName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customer', 'domainName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customer=None, domainName=None):
    url = baseUrl + "customer/{customer}/domains/{domainName}"
    method = "GET"
    return Request(
        method, 
        url.format(['customer', 'domainName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customer=None):
    url = baseUrl + "customer/{customer}/domains"
    method = "POST"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customer=None):
    url = baseUrl + "customer/{customer}/domains"
    method = "GET"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
