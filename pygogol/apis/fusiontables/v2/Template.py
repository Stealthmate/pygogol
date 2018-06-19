from pygogol.core import Request

from Defs import baseUrl

def delete(tableId=None, templateId=None):
    url = baseUrl + "tables/{tableId}/templates/{templateId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['tableId', 'templateId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(tableId=None, templateId=None):
    url = baseUrl + "tables/{tableId}/templates/{templateId}"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId', 'templateId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(tableId=None):
    url = baseUrl + "tables/{tableId}/templates"
    method = "POST"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(tableId=None, maxResults=None, pageToken=None):
    url = baseUrl + "tables/{tableId}/templates"
    method = "GET"
    return Request(
        method, 
        url.format(['tableId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(tableId=None, templateId=None):
    url = baseUrl + "tables/{tableId}/templates/{templateId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['tableId', 'templateId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(tableId=None, templateId=None):
    url = baseUrl + "tables/{tableId}/templates/{templateId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['tableId', 'templateId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
