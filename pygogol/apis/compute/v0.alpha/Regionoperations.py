from pygogol.core import Request

from Defs import baseUrl

def delete(operation=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/operations/{operation}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['operation', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(operation=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/operations/{operation}"
    method = "GET"
    return Request(
        method, 
        url.format(['operation', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/operations"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def wait(operation=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/operations/{operation}/wait"
    method = "POST"
    return Request(
        method, 
        url.format(['operation', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
