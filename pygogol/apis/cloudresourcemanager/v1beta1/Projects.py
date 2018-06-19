from pygogol.core import Request

from Defs import baseUrl

def create(useLegacyStack=None):
    url = baseUrl + "v1beta1/projects"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getAncestry(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}:getAncestry"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(resource=None):
    url = baseUrl + "v1beta1/projects/{resource}:getIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1beta1/projects"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(resource=None):
    url = baseUrl + "v1beta1/projects/{resource}:setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(resource=None):
    url = baseUrl + "v1beta1/projects/{resource}:testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def undelete(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}:undelete"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
