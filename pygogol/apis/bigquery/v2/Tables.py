from pygogol.core import Request

from Defs import baseUrl

def delete(datasetId=None, projectId=None, tableId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables/{tableId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['datasetId', 'projectId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(datasetId=None, projectId=None, tableId=None, selectedFields=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables/{tableId}"
    method = "GET"
    return Request(
        method, 
        url.format(['datasetId', 'projectId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(datasetId=None, projectId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables"
    method = "POST"
    return Request(
        method, 
        url.format(['datasetId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(datasetId=None, projectId=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables"
    method = "GET"
    return Request(
        method, 
        url.format(['datasetId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(datasetId=None, projectId=None, tableId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables/{tableId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['datasetId', 'projectId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(datasetId=None, projectId=None, tableId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables/{tableId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['datasetId', 'projectId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
