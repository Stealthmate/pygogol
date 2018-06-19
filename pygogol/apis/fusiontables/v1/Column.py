from pygogol.core import Request

from Defs import baseUrl

def delete(columnId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/columns/{columnId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['columnId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(columnId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/columns/{columnId}"
    method = "GET"
    return Request(
        method, 
        url.format(['columnId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(tableId=None):
    url = baseUrl + "tables/{tableId}/columns"
    method = "POST"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(tableId=None, maxResults=None, pageToken=None):
    url = baseUrl + "tables/{tableId}/columns"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(columnId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/columns/{columnId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['columnId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(columnId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/columns/{columnId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['columnId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
