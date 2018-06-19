from pygogol.core import Request

from Defs import baseUrl

def delete(address=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/addresses/{address}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['address', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(address=None, project=None):
    url = baseUrl + "{project}/global/addresses/{address}"
    method = "GET"
    return Request(
        method, 
        url.format(['address', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/addresses"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/addresses"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, resource=None):
    url = baseUrl + "{project}/global/addresses/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/addresses/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
