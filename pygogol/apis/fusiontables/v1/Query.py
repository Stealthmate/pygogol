from pygogol.core import Request

from Defs import baseUrl

def sql(hdrs=None, sql=None, typed=None):
    url = baseUrl + "query"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def sqlGet(hdrs=None, sql=None, typed=None):
    url = baseUrl + "query"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
