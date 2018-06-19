from pygogol.core import Request

from Defs import baseUrl

def delete(alertId=None):
    url = baseUrl + "alerts/{alertId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['alertId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(locale=None):
    url = baseUrl + "alerts"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
