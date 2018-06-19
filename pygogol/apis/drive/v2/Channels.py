from pygogol.core import Request

from Defs import baseUrl

def stop():
    url = baseUrl + "channels/stop"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
