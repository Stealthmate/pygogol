from pygogol.core import Request

from Defs import baseUrl

def get(name=None):
    url = baseUrl + "v1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(category=None, curated=None, format=None, keywords=None, maxComplexity=None, orderBy=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/assets"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
