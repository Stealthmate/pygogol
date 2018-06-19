from pygogol.core import Request

from Defs import baseUrl

def getforobserved():
    url = baseUrl + "v1beta1/beaconinfo:getforobserved"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
