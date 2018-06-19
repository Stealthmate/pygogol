from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None):
    url = baseUrl + "blogs/{blogId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
