from pygogol.core import Request

from Defs import baseUrl

def get(instanceGroup=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroups/{instanceGroup}"
    method = "GET"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroups"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listInstances(instanceGroup=None, project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroups/{instanceGroup}/listInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setNamedPorts(instanceGroup=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroups/{instanceGroup}/setNamedPorts"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroup', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroups/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
