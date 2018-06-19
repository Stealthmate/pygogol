from pygogol.core import Request

from Defs import baseUrl

def get(instance=None, operation=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/operations/{operation}"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'operation', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(instance=None, project=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{project}/instances/{instance}/operations"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
