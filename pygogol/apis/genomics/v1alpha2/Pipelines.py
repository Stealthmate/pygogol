from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1alpha2/pipelines"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(pipelineId=None):
    url = baseUrl + "v1alpha2/pipelines/{pipelineId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['pipelineId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(pipelineId=None):
    url = baseUrl + "v1alpha2/pipelines/{pipelineId}"
    method = "GET"
    return Request(
        method, 
        url.format(['pipelineId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getControllerConfig(operationId=None, validationToken=None):
    url = baseUrl + "v1alpha2/pipelines:getControllerConfig"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(namePrefix=None, pageSize=None, pageToken=None, projectId=None):
    url = baseUrl + "v1alpha2/pipelines"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def run():
    url = baseUrl + "v1alpha2/pipelines:run"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setOperationStatus():
    url = baseUrl + "v1alpha2/pipelines:setOperationStatus"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
