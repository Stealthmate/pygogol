from pygogol.core import Request

from Defs import baseUrl

def addPeering(network=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/networks/{network}/addPeering"
    method = "POST"
    return Request(
        method, 
        url.format(['network', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(network=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/networks/{network}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['network', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(network=None, project=None):
    url = baseUrl + "{project}/global/networks/{network}"
    method = "GET"
    return Request(
        method, 
        url.format(['network', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/networks"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/networks"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(network=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/networks/{network}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['network', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removePeering(network=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/networks/{network}/removePeering"
    method = "POST"
    return Request(
        method, 
        url.format(['network', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def switchToCustomMode(network=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/networks/{network}/switchToCustomMode"
    method = "POST"
    return Request(
        method, 
        url.format(['network', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/networks/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
