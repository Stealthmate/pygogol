from pygogol.core import Request

from Defs import baseUrl

def list(customer=None):
    url = baseUrl + "customer/{customer}/roles/ALL/privileges"
    method = "GET"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
