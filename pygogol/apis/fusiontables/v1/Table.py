from pygogol.core import Request

from Defs import baseUrl

def copy(tableId=None, copyPresentation=None):
    url = baseUrl + "tables/{tableId}/copy"
    method = "POST"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(tableId=None):
    url = baseUrl + "tables/{tableId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(tableId=None):
    url = baseUrl + "tables/{tableId}"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def importRows(tableId=None, delimiter=None, encoding=None, endLine=None, isStrict=None, startLine=None):
    url = baseUrl + "tables/{tableId}/import"
    method = "POST"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def importTable(delimiter=None, encoding=None, name=None):
    url = baseUrl + "tables/import"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "tables"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None):
    url = baseUrl + "tables"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(tableId=None, replaceViewDefinition=None):
    url = baseUrl + "tables/{tableId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(tableId=None, replaceViewDefinition=None):
    url = baseUrl + "tables/{tableId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
