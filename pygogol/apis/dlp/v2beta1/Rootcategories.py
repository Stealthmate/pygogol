from pygogol.core import Request

from Defs import baseUrl

def list(languageCode=None):
    url = baseUrl + "v2beta1/rootCategories"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
