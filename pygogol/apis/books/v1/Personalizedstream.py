from pygogol.core import Request

from Defs import baseUrl

def get(locale=None, maxAllowedMaturityRating=None, source=None):
    url = baseUrl + "personalizedstream/get"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
