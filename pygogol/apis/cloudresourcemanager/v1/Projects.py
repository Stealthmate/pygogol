from pygogol.core import Request

from Defs import baseUrl

def clearOrgPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:clearOrgPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/projects"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(projectId=None):
    url = baseUrl + "v1/projects/{projectId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(projectId=None):
    url = baseUrl + "v1/projects/{projectId}"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getAncestry(projectId=None):
    url = baseUrl + "v1/projects/{projectId}:getAncestry"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getEffectiveOrgPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:getEffectiveOrgPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(resource=None):
    url = baseUrl + "v1/projects/{resource}:getIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getOrgPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:getOrgPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/projects"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listAvailableOrgPolicyConstraints(resource=None):
    url = baseUrl + "v1/{+resource}:listAvailableOrgPolicyConstraints"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listOrgPolicies(resource=None):
    url = baseUrl + "v1/{+resource}:listOrgPolicies"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(resource=None):
    url = baseUrl + "v1/projects/{resource}:setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setOrgPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:setOrgPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(resource=None):
    url = baseUrl + "v1/projects/{resource}:testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def undelete(projectId=None):
    url = baseUrl + "v1/projects/{projectId}:undelete"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(projectId=None):
    url = baseUrl + "v1/projects/{projectId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
