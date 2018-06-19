from pygogol.core import Request

from Defs import baseUrl

def search(ids=None, indent=None, languages=None, limit=None, prefix=None, query=None, types=None):
    url = baseUrl + "v1/entities:search"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
