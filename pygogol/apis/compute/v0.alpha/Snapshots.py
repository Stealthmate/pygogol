from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, snapshot=None, requestId=None):
    url = baseUrl + "{project}/global/snapshots/{snapshot}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'snapshot']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, snapshot=None):
    url = baseUrl + "{project}/global/snapshots/{snapshot}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'snapshot']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/snapshots/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/snapshots"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/snapshots/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, resource=None):
    url = baseUrl + "{project}/global/snapshots/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/snapshots/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
