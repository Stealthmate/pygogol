from pygogol.core import Request

from Defs import baseUrl

def disable(name=None):
    url = baseUrl + "v1/{+name}:disable"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def enable(name=None):
    url = baseUrl + "v1/{+name}:enable"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listEnabled(parent=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/{+parent}/services:enabled"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search(pageSize=None, pageToken=None):
    url = baseUrl + "v1/services:search"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
