from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, range=None):
    url = baseUrl + "blogs/{blogId}/pageviews"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
