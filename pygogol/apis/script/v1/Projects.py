from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/projects"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(scriptId=None):
    url = baseUrl + "v1/projects/{scriptId}"
    method = "GET"
    return Request(
        method, 
        url.format(['scriptId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getContent(scriptId=None, versionNumber=None):
    url = baseUrl + "v1/projects/{scriptId}/content"
    method = "GET"
    return Request(
        method, 
        url.format(['scriptId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getMetrics(scriptId=None, metricsFilter.deploymentId=None, metricsGranularity=None):
    url = baseUrl + "v1/projects/{scriptId}/metrics"
    method = "GET"
    return Request(
        method, 
        url.format(['scriptId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateContent(scriptId=None):
    url = baseUrl + "v1/projects/{scriptId}/content"
    method = "PUT"
    return Request(
        method, 
        url.format(['scriptId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
