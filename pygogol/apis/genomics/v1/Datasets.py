from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/datasets"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(datasetId=None):
    url = baseUrl + "v1/datasets/{datasetId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['datasetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(datasetId=None):
    url = baseUrl + "v1/datasets/{datasetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['datasetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:getIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None, projectId=None):
    url = baseUrl + "v1/datasets"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(datasetId=None, updateMask=None):
    url = baseUrl + "v1/datasets/{datasetId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['datasetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(resource=None):
    url = baseUrl + "v1/{+resource}:testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def undelete(datasetId=None):
    url = baseUrl + "v1/datasets/{datasetId}:undelete"
    method = "POST"
    return Request(
        method, 
        url.format(['datasetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
