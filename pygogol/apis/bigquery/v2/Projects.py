from pygogol.core import Request

from Defs import baseUrl

def getServiceAccount(projectId=None):
    url = baseUrl + "projects/{projectId}/serviceAccount"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None):
    url = baseUrl + "projects"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
