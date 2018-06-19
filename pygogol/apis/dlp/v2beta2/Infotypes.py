from pygogol.core import Request

from Defs import baseUrl

def list(filter=None, languageCode=None):
    url = baseUrl + "v2beta2/infoTypes"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
