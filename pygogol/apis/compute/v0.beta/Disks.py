from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/disks"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def createSnapshot(disk=None, project=None, zone=None, guestFlush=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/disks/{disk}/createSnapshot"
    method = "POST"
    return Request(
        method, 
        url.format(['disk', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(disk=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/disks/{disk}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['disk', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(disk=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/disks/{disk}"
    method = "GET"
    return Request(
        method, 
        url.format(['disk', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None, sourceImage=None):
    url = baseUrl + "{project}/zones/{zone}/disks"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/disks"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resize(disk=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/disks/{disk}/resize"
    method = "POST"
    return Request(
        method, 
        url.format(['disk', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, resource=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/disks/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/disks/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
