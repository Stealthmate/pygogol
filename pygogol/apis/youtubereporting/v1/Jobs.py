from pygogol.core import Request

from Defs import baseUrl

def create(onBehalfOfContentOwner=None):
    url = baseUrl + "v1/jobs"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(jobId=None, onBehalfOfContentOwner=None):
    url = baseUrl + "v1/jobs/{jobId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['jobId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(jobId=None, onBehalfOfContentOwner=None):
    url = baseUrl + "v1/jobs/{jobId}"
    method = "GET"
    return Request(
        method, 
        url.format(['jobId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(includeSystemManaged=None, onBehalfOfContentOwner=None, pageSize=None, pageToken=None):
    url = baseUrl + "v1/jobs"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
