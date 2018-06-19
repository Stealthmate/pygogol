from pygogol.core import Request

from Defs import baseUrl

def delete(blogId=None, pageId=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(blogId=None, pageId=None, view=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(blogId=None, isDraft=None):
    url = baseUrl + "blogs/{blogId}/pages"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(blogId=None, fetchBodies=None, maxResults=None, pageToken=None, status=None, view=None):
    url = baseUrl + "blogs/{blogId}/pages"
    method = "GET"
    return Request(
        method, 
        url.format(['blogId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(blogId=None, pageId=None, publish=None, revert=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def publish(blogId=None, pageId=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}/publish"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def revert(blogId=None, pageId=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}/revert"
    method = "POST"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(blogId=None, pageId=None, publish=None, revert=None):
    url = baseUrl + "blogs/{blogId}/pages/{pageId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['blogId', 'pageId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
