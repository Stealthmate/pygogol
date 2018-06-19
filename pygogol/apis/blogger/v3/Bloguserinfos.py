from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, userId=None, maxPosts=None):
    url = baseUrl + "users/{userId}/blogs/{blogId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
