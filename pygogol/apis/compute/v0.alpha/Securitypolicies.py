from pygogol.core import Request

from Defs import baseUrl

def addRule(project=None, securityPolicy=None, validateOnly=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}/addRule"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, securityPolicy=None, requestId=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, securityPolicy=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getRule(project=None, securityPolicy=None, priority=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}/getRule"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None, validateOnly=None):
    url = baseUrl + "{project}/global/securityPolicies"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/securityPolicies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listPreconfiguredExpressionSets(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/securityPolicies/listPreconfiguredExpressionSets"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, securityPolicy=None, requestId=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patchRule(project=None, securityPolicy=None, priority=None, validateOnly=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}/patchRule"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeRule(project=None, securityPolicy=None, priority=None):
    url = baseUrl + "{project}/global/securityPolicies/{securityPolicy}/removeRule"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'securityPolicy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, resource=None):
    url = baseUrl + "{project}/global/securityPolicies/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/securityPolicies/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
