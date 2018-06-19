from pygogol.core import Request

from Defs import baseUrl

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

def update(backendService=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendServices/{backendService}"
    method = "PUT"
    return Request(
        method, 
        url.format(['backendService', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
