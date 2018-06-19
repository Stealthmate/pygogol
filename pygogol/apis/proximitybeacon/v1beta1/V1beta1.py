from pygogol.core import Request

from Defs import baseUrl

def getEidparams():
    url = baseUrl + "v1beta1/eidparams"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
