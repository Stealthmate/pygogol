from pygogol.core import Request

from Defs import baseUrl

def stop():
    url = baseUrl + "/admin/directory_v1/channels/stop"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
