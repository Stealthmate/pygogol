from pygogol.core import Request

from Defs import baseUrl

def create(project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(managedZone=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(managedZone=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}"
    method = "GET"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, dnsName=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/managedZones"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(managedZone=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(managedZone=None, project=None, clientOperationId=None):
    url = baseUrl + "{project}/managedZones/{managedZone}"
    method = "PUT"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
