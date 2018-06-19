from pygogol.core import Request

from Defs import baseUrl

def createContact(parent=None):
    url = baseUrl + "v1/people:createContact"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteContact(resourceName=None):
    url = baseUrl + "v1/{+resourceName}:deleteContact"
    method = "DELETE"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(resourceName=None, personFields=None, requestMask.includeField=None):
    url = baseUrl + "v1/{+resourceName}"
    method = "GET"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getBatchGet(personFields=None, requestMask.includeField=None, resourceNames=None):
    url = baseUrl + "v1/people:batchGet"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateContact(resourceName=None, updatePersonFields=None):
    url = baseUrl + "v1/{+resourceName}:updateContact"
    method = "PATCH"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
