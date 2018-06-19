from pygogol.core import Request

from Defs import baseUrl

def create(managedZone=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/changes"
    method = "POST"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(changeId=None, managedZone=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/changes/{changeId}"
    method = "GET"
    return Request(
        method, 
        url.format(['changeId', 'managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(managedZone=None, project=None, maxResults=None, pageToken=None, sortBy=None, sortOrder=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/changes"
    method = "GET"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
