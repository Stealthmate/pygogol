from pygogol.core import Request

from Defs import baseUrl

def batchDelete():
    url = baseUrl + "v2/jobs:batchDelete"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v2/jobs"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(name=None, disableFastProcess=None):
    url = baseUrl + "v2/{+name}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteByFilter():
    url = baseUrl + "v2/jobs:deleteByFilter"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v2/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def histogram():
    url = baseUrl + "v2/jobs:histogram"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, idsOnly=None, pageSize=None, pageToken=None):
    url = baseUrl + "v2/jobs"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(name=None):
    url = baseUrl + "v2/{+name}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v2/jobs:search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def searchForAlert():
    url = baseUrl + "v2/jobs:searchForAlert"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
