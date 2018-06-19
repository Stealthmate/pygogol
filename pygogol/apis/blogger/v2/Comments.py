from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, commentId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments/{commentId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'commentId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, postId=None, fetchBodies=None, maxResults=None, pageToken=None, startDate=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
