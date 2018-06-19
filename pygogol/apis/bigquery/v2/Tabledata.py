from pygogol.core import Request

from Defs import baseUrl

def insertAll(datasetId=None, projectId=None, tableId=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll"
    method = "POST"
    return Request(
        method, 
        url.format(['datasetId', 'projectId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(datasetId=None, projectId=None, tableId=None, maxResults=None, pageToken=None, selectedFields=None, startIndex=None):
    url = baseUrl + "projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data"
    method = "GET"
    return Request(
        method, 
        url.format(['datasetId', 'projectId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
