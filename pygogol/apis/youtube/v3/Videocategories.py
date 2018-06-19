from pygogol.core import Request

from Defs import baseUrl

def list(hl=None, id=None, part=None, regionCode=None):
    url = baseUrl + "videoCategories"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
