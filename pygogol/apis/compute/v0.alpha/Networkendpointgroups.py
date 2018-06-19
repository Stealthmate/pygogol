from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/networkEndpointGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def attachNetworkEndpoints(networkEndpointGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}/attachNetworkEndpoints"
    method = "POST"
    return Request(
        method, 
        url.format(['networkEndpointGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(networkEndpointGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['networkEndpointGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def detachNetworkEndpoints(networkEndpointGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}/detachNetworkEndpoints"
    method = "POST"
    return Request(
        method, 
        url.format(['networkEndpointGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(networkEndpointGroup=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}"
    method = "GET"
    return Request(
        method, 
        url.format(['networkEndpointGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listNetworkEndpoints(networkEndpointGroup=None, project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups/{networkEndpointGroup}/listNetworkEndpoints"
    method = "POST"
    return Request(
        method, 
        url.format(['networkEndpointGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/networkEndpointGroups/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
