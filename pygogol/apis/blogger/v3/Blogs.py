from pygogol.core import Request

from Defs import baseUrl

def get(blogId=None, maxPosts=None, view=None):
    url = baseUrl + "blogs/{blogId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getByUrl(url=None, view=None):
    url = baseUrl + "blogs/byurl"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listByUser(userId=None, fetchUserInfo=None, role=None, status=None, view=None):
    url = baseUrl + "users/{userId}/blogs"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
