from pygogol.core import Request

from Defs import baseUrl

def approve(blogId=None, commentId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments/{commentId}/approve"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'commentId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(blogId=None, commentId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments/{commentId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['blogId', 'commentId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(blogId=None, commentId=None, postId=None, view=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments/{commentId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'commentId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, postId=None, endDate=None, fetchBodies=None, maxResults=None, pageToken=None, startDate=None, status=None, view=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listByBlog(blogId=None, endDate=None, fetchBodies=None, maxResults=None, pageToken=None, startDate=None, status=None):
    url = baseUrl + "blogs/{blogId}/comments"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def markAsSpam(blogId=None, commentId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments/{commentId}/spam"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'commentId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeContent(blogId=None, commentId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/comments/{commentId}/removecontent"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'commentId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
