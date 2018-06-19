from pygogol.core import Request

from Defs import baseUrl

def get(name=None):
    url = baseUrl + "v1beta1/operations/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
