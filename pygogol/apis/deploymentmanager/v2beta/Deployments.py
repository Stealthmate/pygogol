from pygogol.core import Request

from Defs import baseUrl

def cancelPreview(deployment=None, project=None):
    url = baseUrl + "{project}/global/deployments/{deployment}/cancelPreview"
    method = "POST"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(deployment=None, project=None, deletePolicy=None):
    url = baseUrl + "{project}/global/deployments/{deployment}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(deployment=None, project=None):
    url = baseUrl + "{project}/global/deployments/{deployment}"
    method = "GET"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/deployments/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, createPolicy=None, preview=None):
    url = baseUrl + "{project}/global/deployments"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/deployments"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(deployment=None, project=None, createPolicy=None, deletePolicy=None, preview=None):
    url = baseUrl + "{project}/global/deployments/{deployment}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/deployments/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def stop(deployment=None, project=None):
    url = baseUrl + "{project}/global/deployments/{deployment}/stop"
    method = "POST"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/deployments/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(deployment=None, project=None, createPolicy=None, deletePolicy=None, preview=None):
    url = baseUrl + "{project}/global/deployments/{deployment}"
    method = "PUT"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
