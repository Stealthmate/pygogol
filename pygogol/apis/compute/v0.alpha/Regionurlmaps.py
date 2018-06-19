from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, region=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps/{urlMap}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, urlMap=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps/{urlMap}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, region=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps/{urlMap}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'region', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, region=None, urlMap=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps/{urlMap}"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'region', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def validate(project=None, region=None, urlMap=None):
    url = baseUrl + "{project}/regions/{region}/urlMaps/{urlMap}/validate"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'urlMap']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
