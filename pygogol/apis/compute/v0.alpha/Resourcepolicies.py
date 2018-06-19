from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/resourcePolicies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, region=None, resourcePolicy=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies/{resourcePolicy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'resourcePolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, resourcePolicy=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies/{resourcePolicy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'resourcePolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/resourcePolicies/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
