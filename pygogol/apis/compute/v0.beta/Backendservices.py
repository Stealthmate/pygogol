from pygogol.core import Request

from Defs import baseUrl

def addSignedUrlKey(backendService=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}/addSignedUrlKey"
    method = "POST"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/backendServices"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(backendService=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteSignedUrlKey(backendService=None, project=None, keyName=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}/deleteSignedUrlKey"
    method = "POST"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(backendService=None, project=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}"
    method = "GET"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getHealth(backendService=None, project=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}/getHealth"
    method = "POST"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/backendServices"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(backendService=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setSecurityPolicy(backendService=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}/setSecurityPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/backendServices/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(backendService=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}"
    method = "PUT"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
