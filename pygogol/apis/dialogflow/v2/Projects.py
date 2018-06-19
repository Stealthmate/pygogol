from pygogol.core import Request

from Defs import baseUrl

def getAgent(parent=None):
    url = baseUrl + "v2/{+parent}/agent"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
