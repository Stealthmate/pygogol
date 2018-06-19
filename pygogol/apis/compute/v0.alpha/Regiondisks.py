from pygogol.core import Request

from Defs import baseUrl

def createSnapshot(disk=None, project=None, region=None, guestFlush=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/disks/{disk}/createSnapshot"
    method = "POST"
    return Request(
        method, 
        url.format(['disk', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(disk=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/disks/{disk}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['disk', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(disk=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/disks/{disk}"
    method = "GET"
    return Request(
        method, 
        url.format(['disk', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None, sourceImage=None):
    url = baseUrl + "{project}/regions/{region}/disks"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/disks"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resize(disk=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/disks/{disk}/resize"
    method = "POST"
    return Request(
        method, 
        url.format(['disk', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, region=None, resource=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/disks/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/disks/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
