from pygogol.core import Request

from Defs import baseUrl

def get(managedZone=None, operation=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/operations/{operation}"
    method = "GET"
    return Request(
        method, 
        url.format(['managedZone', 'operation', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(managedZone=None, project=None, maxResults=None, pageToken=None, sortBy=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/operations"
    method = "GET"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
