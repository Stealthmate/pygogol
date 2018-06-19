from pygogol.core import Request

from Defs import baseUrl

def delete(customer=None, domainAliasName=None):
    url = baseUrl + "customer/{customer}/domainaliases/{domainAliasName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customer', 'domainAliasName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customer=None, domainAliasName=None):
    url = baseUrl + "customer/{customer}/domainaliases/{domainAliasName}"
    method = "GET"
    return Request(
        method, 
        url.format(['customer', 'domainAliasName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customer=None):
    url = baseUrl + "customer/{customer}/domainaliases"
    method = "POST"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customer=None, parentDomainName=None):
    url = baseUrl + "customer/{customer}/domainaliases"
    method = "GET"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
