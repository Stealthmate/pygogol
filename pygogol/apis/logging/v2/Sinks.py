from pygogol.core import Request

from Defs import baseUrl

def create(parent=None, uniqueWriterIdentity=None):
    url = baseUrl + "v2/{+parent}/sinks"
    method = "POST"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(sinkName=None):
    url = baseUrl + "v2/{+sinkName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['sinkName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(sinkName=None):
    url = baseUrl + "v2/{+sinkName}"
    method = "GET"
    return Request(
        method, 
        url.format(['sinkName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(parent=None, pageSize=None, pageToken=None):
    url = baseUrl + "v2/{+parent}/sinks"
    method = "GET"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(sinkName=None, uniqueWriterIdentity=None, updateMask=None):
    url = baseUrl + "v2/{+sinkName}"
    method = "PUT"
    return Request(
        method, 
        url.format(['sinkName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
