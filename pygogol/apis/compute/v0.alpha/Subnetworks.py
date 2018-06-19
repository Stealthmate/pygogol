from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/subnetworks"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, region=None, subnetwork=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{subnetwork}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'subnetwork']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def expandIpCidrRange(project=None, region=None, subnetwork=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{subnetwork}/expandIpCidrRange"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'subnetwork']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, subnetwork=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{subnetwork}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'subnetwork']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listUsable(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/subnetworks/listUsable"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, region=None, subnetwork=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{subnetwork}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'region', 'subnetwork']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setPrivateIpGoogleAccess(project=None, region=None, subnetwork=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{subnetwork}/setPrivateIpGoogleAccess"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'subnetwork']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/subnetworks/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
