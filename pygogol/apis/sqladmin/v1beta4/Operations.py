from pygogol.core import Request

from Defs import baseUrl

def get(operation=None, project=None):
    url = baseUrl + "projects/{project}/operations/{operation}"
    method = "GET"
    return Request(
        method, 
        url.format(['operation', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, instance=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{project}/operations"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
