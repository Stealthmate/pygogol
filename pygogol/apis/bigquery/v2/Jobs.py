from pygogol.core import Request

from Defs import baseUrl

def cancel(jobId=None, projectId=None, location=None):
    url = baseUrl + "projects/{projectId}/jobs/{jobId}/cancel"
    method = "POST"
    return Request(
        method, 
        url.format(['jobId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(jobId=None, projectId=None, location=None):
    url = baseUrl + "projects/{projectId}/jobs/{jobId}"
    method = "GET"
    return Request(
        method, 
        url.format(['jobId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getQueryResults(jobId=None, projectId=None, location=None, maxResults=None, pageToken=None, startIndex=None, timeoutMs=None):
    url = baseUrl + "projects/{projectId}/queries/{jobId}"
    method = "GET"
    return Request(
        method, 
        url.format(['jobId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(projectId=None):
    url = baseUrl + "projects/{projectId}/jobs"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(projectId=None, allUsers=None, maxCreationTime=None, maxResults=None, minCreationTime=None, pageToken=None, projection=None, stateFilter=None):
    url = baseUrl + "projects/{projectId}/jobs"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def query(projectId=None):
    url = baseUrl + "projects/{projectId}/queries"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
