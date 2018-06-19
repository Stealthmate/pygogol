from pygogol.core import Request

from Defs import baseUrl

def analyze(id=None, project=None):
    url = baseUrl + "{project}/trainedmodels/{id}/analyze"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(id=None, project=None):
    url = baseUrl + "{project}/trainedmodels/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None, project=None):
    url = baseUrl + "{project}/trainedmodels/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "{project}/trainedmodels"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/trainedmodels/list"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def predict(id=None, project=None):
    url = baseUrl + "{project}/trainedmodels/{id}/predict"
    method = "POST"
    return Request(
        method, 
        url.format(['id', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(id=None, project=None):
    url = baseUrl + "{project}/trainedmodels/{id}"
    method = "PUT"
    return Request(
        method, 
        url.format(['id', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
