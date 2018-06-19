from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/services"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def disable(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:disable"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def enable(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:enable"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generateConfigReport():
    url = baseUrl + "v1/services:generateConfigReport"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}"
    method = "GET"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getConfig(serviceName=None, configId=None, view=None):
    url = baseUrl + "v1/services/{serviceName}/config"
    method = "GET"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
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

def list(consumerId=None, pageSize=None, pageToken=None, producerProjectId=None):
    url = baseUrl + "v1/services"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
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

def undelete(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:undelete"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
