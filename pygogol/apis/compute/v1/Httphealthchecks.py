from pygogol.core import Request

from Defs import baseUrl

def delete(httpHealthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/httpHealthChecks/{httpHealthCheck}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['httpHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(httpHealthCheck=None, project=None):
    url = baseUrl + "{project}/global/httpHealthChecks/{httpHealthCheck}"
    method = "GET"
    return Request(
        method, 
        url.format(['httpHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/httpHealthChecks"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/httpHealthChecks"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(httpHealthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/httpHealthChecks/{httpHealthCheck}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['httpHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(httpHealthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/httpHealthChecks/{httpHealthCheck}"
    method = "PUT"
    return Request(
        method, 
        url.format(['httpHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
