from pygogol.core import Request

from Defs import baseUrl

def delete(styleId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/styles/{styleId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['styleId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(styleId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/styles/{styleId}"
    method = "GET"
    return Request(
        method, 
        url.format(['styleId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(tableId=None):
    url = baseUrl + "tables/{tableId}/styles"
    method = "POST"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(tableId=None, maxResults=None, pageToken=None):
    url = baseUrl + "tables/{tableId}/styles"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(styleId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/styles/{styleId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['styleId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(styleId=None, tableId=None):
    url = baseUrl + "tables/{tableId}/styles/{styleId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['styleId', 'tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
