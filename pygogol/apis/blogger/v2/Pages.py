from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, pageId=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, fetchBodies=None):
    url = baseUrl + "blogs/{blogId}/pages"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
