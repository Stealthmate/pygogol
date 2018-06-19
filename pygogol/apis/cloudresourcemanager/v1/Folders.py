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

def getEffectiveOrgPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:getEffectiveOrgPolicy"
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

def setOrgPolicy(resource=None):
    url = baseUrl + "v1/{+resource}:setOrgPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
