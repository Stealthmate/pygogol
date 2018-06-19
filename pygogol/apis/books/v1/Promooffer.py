from pygogol.core import Request

from Defs import baseUrl

def accept(androidId=None, device=None, manufacturer=None, model=None, offerId=None, product=None, serial=None, volumeId=None):
    url = baseUrl + "promooffer/accept"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def dismiss(androidId=None, device=None, manufacturer=None, model=None, offerId=None, product=None, serial=None):
    url = baseUrl + "promooffer/dismiss"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(androidId=None, device=None, manufacturer=None, model=None, product=None, serial=None):
    url = baseUrl + "promooffer/get"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
