from pygogol.core import Request

from Defs import baseUrl

def getRest(api=None, version=None):
    url = baseUrl + "apis/{api}/{version}/rest"
    method = "GET"
    return Request(
        method, 
        url.format(['api', 'version']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(name=None, preferred=None):
    url = baseUrl + "apis"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
