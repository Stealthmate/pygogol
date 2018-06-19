from pygogol.core import Request

from Defs import baseUrl

def batchGet(maxMembers=None, resourceNames=None):
    url = baseUrl + "v1/contactGroups:batchGet"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1/contactGroups"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(resourceName=None, deleteContacts=None):
    url = baseUrl + "v1/{+resourceName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(resourceName=None, maxMembers=None):
    url = baseUrl + "v1/{+resourceName}"
    method = "GET"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None, syncToken=None):
    url = baseUrl + "v1/contactGroups"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(resourceName=None):
    url = baseUrl + "v1/{+resourceName}"
    method = "PUT"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
