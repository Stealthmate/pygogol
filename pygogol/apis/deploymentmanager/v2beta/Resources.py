from pygogol.core import Request

from Defs import baseUrl

def get(deployment=None, project=None, resource=None):
    url = baseUrl + "{project}/global/deployments/{deployment}/resources/{resource}"
    method = "GET"
    return Request(
        method, 
        url.format(['deployment', 'project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(deployment=None, project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/deployments/{deployment}/resources"
    method = "GET"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
