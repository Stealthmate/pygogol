from pygogol.core import Request

from Defs import baseUrl

def find():
    url = baseUrl + "v4/fullHashes:find"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
