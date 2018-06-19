from pygogol.core import Request

from Defs import baseUrl

def delete(httpsHealthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/httpsHealthChecks/{httpsHealthCheck}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['httpsHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(httpsHealthCheck=None, project=None):
    url = baseUrl + "{project}/global/httpsHealthChecks/{httpsHealthCheck}"
    method = "GET"
    return Request(
        method, 
        url.format(['httpsHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/httpsHealthChecks"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/httpsHealthChecks"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(httpsHealthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/httpsHealthChecks/{httpsHealthCheck}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['httpsHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(httpsHealthCheck=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/httpsHealthChecks/{httpsHealthCheck}"
    method = "PUT"
    return Request(
        method, 
        url.format(['httpsHealthCheck', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
