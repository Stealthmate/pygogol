from pygogol.core import Request

from Defs import baseUrl

def complete(companyName=None, languageCode=None, pageSize=None, query=None, scope=None, type=None):
    url = baseUrl + "v2:complete"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
