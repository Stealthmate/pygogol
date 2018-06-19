from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/hosts"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(host=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/hosts/{host}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['host', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(host=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/hosts/{host}"
    method = "GET"
    return Request(
        method, 
        url.format(['host', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/hosts/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/hosts"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/hosts"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/hosts/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/hosts/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
