from pygogol.core import Request

from Defs import baseUrl

def batchEnable(parent=None):
    url = baseUrl + "v1beta1/{+parent}/services:batchEnable"
    method = "POST"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def disable(name=None):
    url = baseUrl + "v1beta1/{+name}:disable"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def enable(name=None):
    url = baseUrl + "v1beta1/{+name}:enable"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v1beta1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(parent=None, filter=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1beta1/{+parent}/services"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
