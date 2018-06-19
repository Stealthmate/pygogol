from pygogol.core import Request

from Defs import baseUrl

def analyze(id=None):
    url = baseUrl + "trainedmodels/{id}/analyze"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(id=None):
    url = baseUrl + "trainedmodels/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None):
    url = baseUrl + "trainedmodels/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "trainedmodels"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None):
    url = baseUrl + "trainedmodels/list"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def predict(id=None):
    url = baseUrl + "trainedmodels/{id}/predict"
    method = "POST"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None):
    url = baseUrl + "trainedmodels/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
