from pygogol.core import Request

from Defs import baseUrl

def delete(backendService=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/backendServices/{backendService}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['backendService', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(backendService=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/backendServices/{backendService}"
    method = "GET"
    return Request(
        method, 
        url.format(['backendService', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getHealth(backendService=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/backendServices/{backendService}/getHealth"
    method = "POST"
    return Request(
        method, 
        url.format(['backendService', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/backendServices"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/backendServices"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(backendService=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/backendServices/{backendService}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['backendService', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(backendService=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/backendServices/{backendService}"
    method = "PUT"
    return Request(
        method, 
        url.format(['backendService', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
