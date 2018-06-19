from pygogol.core import Request

from Defs import baseUrl

def get(name=None, organizationId=None):
    url = baseUrl + "v1beta1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(resource=None):
    url = baseUrl + "v1beta1/{+resource}:getIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1beta1/organizations"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(resource=None):
    url = baseUrl + "v1beta1/{+resource}:setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(resource=None):
    url = baseUrl + "v1beta1/{+resource}:testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(name=None):
    url = baseUrl + "v1beta1/{+name}"
    method = "PUT"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
