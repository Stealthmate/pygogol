from pygogol.core import Request

from Defs import baseUrl

def analyzeEntities():
    url = baseUrl + "v1/documents:analyzeEntities"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def analyzeEntitySentiment():
    url = baseUrl + "v1/documents:analyzeEntitySentiment"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def analyzeSentiment():
    url = baseUrl + "v1/documents:analyzeSentiment"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def analyzeSyntax():
    url = baseUrl + "v1/documents:analyzeSyntax"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def annotateText():
    url = baseUrl + "v1/documents:annotateText"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def classifyText():
    url = baseUrl + "v1/documents:classifyText"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
