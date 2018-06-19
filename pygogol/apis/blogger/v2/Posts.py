from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, fetchBodies=None, maxResults=None, pageToken=None, startDate=None):
    url = baseUrl + "blogs/{blogId}/posts"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
