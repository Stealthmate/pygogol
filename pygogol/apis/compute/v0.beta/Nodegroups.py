from pygogol.core import Request

from Defs import baseUrl

def addNodes(nodeGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{nodeGroup}/addNodes"
    method = "POST"
    return Request(
        method, 
        url.format(['nodeGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/nodeGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(nodeGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{nodeGroup}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['nodeGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteNodes(nodeGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{nodeGroup}/deleteNodes"
    method = "POST"
    return Request(
        method, 
        url.format(['nodeGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(nodeGroup=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{nodeGroup}"
    method = "GET"
    return Request(
        method, 
        url.format(['nodeGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, initialNodeCount=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setNodeTemplate(nodeGroup=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{nodeGroup}/setNodeTemplate"
    method = "POST"
    return Request(
        method, 
        url.format(['nodeGroup', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/nodeGroups/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
