from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/autoscalers"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(autoscaler=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers/{autoscaler}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['autoscaler', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(autoscaler=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers/{autoscaler}"
    method = "GET"
    return Request(
        method, 
        url.format(['autoscaler', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, zone=None, autoscaler=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, zone=None, autoscaler=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/autoscalers"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
