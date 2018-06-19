from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/nodeTemplates"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(nodeTemplate=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates/{nodeTemplate}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['nodeTemplate', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(nodeTemplate=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates/{nodeTemplate}"
    method = "GET"
    return Request(
        method, 
        url.format(['nodeTemplate', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/nodeTemplates/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
