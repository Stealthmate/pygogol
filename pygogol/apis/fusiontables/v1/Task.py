from pygogol.core import Request

from Defs import baseUrl

def delete(tableId=None, taskId=None):
    url = baseUrl + "tables/{tableId}/tasks/{taskId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['tableId', 'taskId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(tableId=None, taskId=None):
    url = baseUrl + "tables/{tableId}/tasks/{taskId}"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId', 'taskId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(tableId=None, maxResults=None, pageToken=None, startIndex=None):
    url = baseUrl + "tables/{tableId}/tasks"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
