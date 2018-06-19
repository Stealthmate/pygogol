from pygogol.core import Request

from Defs import baseUrl

def batchUpdate(spreadsheetId=None):
    url = baseUrl + "v4/spreadsheets/{spreadsheetId}:batchUpdate"
    method = "POST"
    return Request(
        method, 
        url.format(['spreadsheetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v4/spreadsheets"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(spreadsheetId=None, includeGridData=None, ranges=None):
    url = baseUrl + "v4/spreadsheets/{spreadsheetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['spreadsheetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getByDataFilter(spreadsheetId=None):
    url = baseUrl + "v4/spreadsheets/{spreadsheetId}:getByDataFilter"
    method = "POST"
    return Request(
        method, 
        url.format(['spreadsheetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
