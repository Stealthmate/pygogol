from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, postId=None, userId=None, maxComments=None):
    url = baseUrl + "users/{userId}/blogs/{blogId}/posts/{postId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'postId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, userId=None, endDate=None, fetchBodies=None, labels=None, maxResults=None, orderBy=None, pageToken=None, startDate=None, status=None, view=None):
    url = baseUrl + "users/{userId}/blogs/{blogId}/posts"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
