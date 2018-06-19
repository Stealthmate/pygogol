from pygogol.core import Request

from Defs import baseUrl

def delete(operation=None, project=None):
    url = baseUrl + "{project}/global/operations/{operation}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['operation', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(operation=None, project=None):
    url = baseUrl + "{project}/global/operations/{operation}"
    method = "GET"
    return Request(
        method, 
        url.format(['operation', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/operations"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
