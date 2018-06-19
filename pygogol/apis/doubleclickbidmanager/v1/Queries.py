from pygogol.core import Request

from Defs import baseUrl

def createquery():
    url = baseUrl + "query"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deletequery(queryId=None):
    url = baseUrl + "query/{queryId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['queryId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getquery(queryId=None):
    url = baseUrl + "query/{queryId}"
    method = "GET"
    return Request(
        method, 
        url.format(['queryId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listqueries():
    url = baseUrl + "queries"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def runquery(queryId=None):
    url = baseUrl + "query/{queryId}"
    method = "POST"
    return Request(
        method, 
        url.format(['queryId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
