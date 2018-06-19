from pygogol.core import Request

from Defs import baseUrl

def downloadlineitems():
    url = baseUrl + "lineitems/downloadlineitems"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def uploadlineitems():
    url = baseUrl + "lineitems/uploadlineitems"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
