from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/forwardingRules"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(forwardingRule=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules/{forwardingRule}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['forwardingRule', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(forwardingRule=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules/{forwardingRule}"
    method = "GET"
    return Request(
        method, 
        url.format(['forwardingRule', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, region=None, resource=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setTarget(forwardingRule=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules/{forwardingRule}/setTarget"
    method = "POST"
    return Request(
        method, 
        url.format(['forwardingRule', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/forwardingRules/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
