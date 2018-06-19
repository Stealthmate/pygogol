from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, sslPolicy=None, requestId=None):
    url = baseUrl + "{project}/global/sslPolicies/{sslPolicy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'sslPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, sslPolicy=None):
    url = baseUrl + "{project}/global/sslPolicies/{sslPolicy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'sslPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/sslPolicies"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/sslPolicies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listAvailableFeatures(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/sslPolicies/listAvailableFeatures"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, sslPolicy=None, requestId=None):
    url = baseUrl + "{project}/global/sslPolicies/{sslPolicy}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'sslPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/sslPolicies/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
