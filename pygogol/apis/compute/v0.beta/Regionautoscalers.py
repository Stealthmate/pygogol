from pygogol.core import Request

from Defs import baseUrl

def delete(autoscaler=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers/{autoscaler}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['autoscaler', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(autoscaler=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers/{autoscaler}"
    method = "GET"
    return Request(
        method, 
        url.format(['autoscaler', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, region=None, autoscaler=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, region=None, autoscaler=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/autoscalers"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
