from pygogol.core import Request

from Defs import baseUrl

def delete(blogId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(blogId=None, postId=None, fetchBody=None, fetchImages=None, maxComments=None, view=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getByPath(blogId=None, maxComments=None, path=None, view=None):
    url = baseUrl + "blogs/{blogId}/posts/bypath"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(blogId=None, fetchBody=None, fetchImages=None, isDraft=None):
    url = baseUrl + "blogs/{blogId}/posts"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, endDate=None, fetchBodies=None, fetchImages=None, labels=None, maxResults=None, orderBy=None, pageToken=None, startDate=None, status=None, view=None):
    url = baseUrl + "blogs/{blogId}/posts"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(blogId=None, postId=None, fetchBody=None, fetchImages=None, maxComments=None, publish=None, revert=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def publish(blogId=None, postId=None, publishDate=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/publish"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def revert(blogId=None, postId=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}/revert"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search(blogId=None, fetchBodies=None, orderBy=None, q=None):
    url = baseUrl + "blogs/{blogId}/posts/search"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(blogId=None, postId=None, fetchBody=None, fetchImages=None, maxComments=None, publish=None, revert=None):
    url = baseUrl + "blogs/{blogId}/posts/{postId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['blogId', 'postId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
