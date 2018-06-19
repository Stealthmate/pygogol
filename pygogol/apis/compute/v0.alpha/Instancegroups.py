from pygogol.core import Request

from Defs import baseUrl

def addInstances(instanceGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{instanceGroup}/addInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/instanceGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instanceGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{instanceGroup}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instanceGroup=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{instanceGroup}"
    method = "GET"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listInstances(instanceGroup=None, project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{instanceGroup}/listInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeInstances(instanceGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{instanceGroup}/removeInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setNamedPorts(instanceGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{instanceGroup}/setNamedPorts"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroups/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
