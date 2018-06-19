from pygogol.core import Request

from Defs import baseUrl

def get(deployment=None, manifest=None, project=None):
    url = baseUrl + "{project}/global/deployments/{deployment}/manifests/{manifest}"
    method = "GET"
    return Request(
        method, 
        url.format(['deployment', 'manifest', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(deployment=None, project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/deployments/{deployment}/manifests"
    method = "GET"
    return Request(
        method, 
        url.format(['deployment', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
