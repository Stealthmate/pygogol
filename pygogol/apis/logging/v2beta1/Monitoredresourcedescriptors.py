from pygogol.core import Request

from Defs import baseUrl

def list(pageSize=None, pageToken=None):
    url = baseUrl + "v2beta1/monitoredResourceDescriptors"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
