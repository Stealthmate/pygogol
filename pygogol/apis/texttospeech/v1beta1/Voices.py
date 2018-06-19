from pygogol.core import Request

from Defs import baseUrl

def list(languageCode=None):
    url = baseUrl + "v1beta1/voices"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
