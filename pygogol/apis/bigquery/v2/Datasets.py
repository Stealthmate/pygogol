from pygogol.core import Request

from Defs import baseUrl

def delete(datasetId=None, projectId=None, deleteContents=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['datasetId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(datasetId=None, projectId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['datasetId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(projectId=None):
    url = baseUrl + "projects/{projectId}/datasets"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(projectId=None, all=None, filter=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{projectId}/datasets"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(datasetId=None, projectId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['datasetId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(datasetId=None, projectId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['datasetId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
