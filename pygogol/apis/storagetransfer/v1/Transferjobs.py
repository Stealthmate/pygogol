from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/transferJobs"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(jobName=None, projectId=None):
    url = baseUrl + "v1/{+jobName}"
    method = "GET"
    return Request(
        method, 
        url.format(['jobName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(filter=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/transferJobs"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(jobName=None):
    url = baseUrl + "v1/{+jobName}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['jobName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
