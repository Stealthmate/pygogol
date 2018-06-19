from pygogol.core import Request

from Defs import baseUrl

def log():
    url = baseUrl + "v2/clientMessages:log"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
