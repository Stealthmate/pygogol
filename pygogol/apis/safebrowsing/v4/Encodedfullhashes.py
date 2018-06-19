from pygogol.core import Request

from Defs import baseUrl

def get(encodedRequest=None, clientId=None, clientVersion=None):
    url = baseUrl + "v4/encodedFullHashes/{encodedRequest}"
    method = "GET"
    return Request(
        method, 
        url.format(['encodedRequest']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
