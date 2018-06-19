from pygogol.core import Request

from Defs import baseUrl

def addHealthCheck(project=None, region=None, targetPool=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}/addHealthCheck"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def addInstance(project=None, region=None, targetPool=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}/addInstance"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/targetPools"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, region=None, targetPool=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, targetPool=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getHealth(project=None, region=None, targetPool=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}/getHealth"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/targetPools"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeHealthCheck(project=None, region=None, targetPool=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}/removeHealthCheck"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeInstance(project=None, region=None, targetPool=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}/removeInstance"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setBackup(project=None, region=None, targetPool=None, failoverRatio=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{targetPool}/setBackup"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'targetPool']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/targetPools/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
