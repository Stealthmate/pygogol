from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, region=None, targetHttpProxy=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetHttpProxies/{targetHttpProxy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'targetHttpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, targetHttpProxy=None):
    url = baseUrl + "{project}/regions/{region}/targetHttpProxies/{targetHttpProxy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'targetHttpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetHttpProxies"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/targetHttpProxies"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setUrlMap(project=None, region=None, targetHttpProxy=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetHttpProxies/{targetHttpProxy}/setUrlMap"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetHttpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/targetHttpProxies/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
