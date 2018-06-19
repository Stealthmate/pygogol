from pygogol.core import Request

from Defs import baseUrl

def delete(healthCheck=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks/{healthCheck}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['healthCheck', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(healthCheck=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks/{healthCheck}"
    method = "GET"
    return Request(
        method, 
        url.format(['healthCheck', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(healthCheck=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks/{healthCheck}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['healthCheck', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(healthCheck=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/healthChecks/{healthCheck}"
    method = "PUT"
    return Request(
        method, 
        url.format(['healthCheck', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
