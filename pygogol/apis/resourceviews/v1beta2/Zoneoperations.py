from pygogol.core import Request

from Defs import baseUrl

def get(operation=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/operations/{operation}"
    method = "GET"
    return Request(
        method, 
        url.format(['operation', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/operations"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
