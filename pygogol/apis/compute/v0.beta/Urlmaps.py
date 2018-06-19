from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/global/urlMaps/{urlMap}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, urlMap=None):
    url = baseUrl + "{project}/global/urlMaps/{urlMap}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/urlMaps"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def invalidateCache(project=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/global/urlMaps/{urlMap}/invalidateCache"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/urlMaps"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/global/urlMaps/{urlMap}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/urlMaps/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/global/urlMaps/{urlMap}"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def validate(project=None, urlMap=None):
    url = baseUrl + "{project}/global/urlMaps/{urlMap}/validate"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
