from pygogol.core import Request

from Defs import baseUrl

def delete(surveyUrlId=None):
    url = baseUrl + "surveys/{surveyUrlId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['surveyUrlId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(surveyUrlId=None):
    url = baseUrl + "surveys/{surveyUrlId}"
    method = "GET"
    return Request(
        method, 
        url.format(['surveyUrlId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "surveys"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, startIndex=None, token=None):
    url = baseUrl + "surveys"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def start(resourceId=None):
    url = baseUrl + "surveys/{resourceId}/start"
    method = "POST"
    return Request(
        method, 
        url.format(['resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def stop(resourceId=None):
    url = baseUrl + "surveys/{resourceId}/stop"
    method = "POST"
    return Request(
        method, 
        url.format(['resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(surveyUrlId=None):
    url = baseUrl + "surveys/{surveyUrlId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['surveyUrlId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
