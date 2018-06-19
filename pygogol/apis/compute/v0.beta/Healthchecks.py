from pygogol.core import Request

from Defs import baseUrl

def delete(healthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/healthChecks/{healthCheck}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['healthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(healthCheck=None, project=None):
    url = baseUrl + "{project}/global/healthChecks/{healthCheck}"
    method = "GET"
    return Request(
        method, 
        url.format(['healthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/healthChecks"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/healthChecks"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(healthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/healthChecks/{healthCheck}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['healthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/healthChecks/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(healthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/healthChecks/{healthCheck}"
    method = "PUT"
    return Request(
        method, 
        url.format(['healthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
