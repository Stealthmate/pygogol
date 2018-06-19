from pygogol.core import Request

from Defs import baseUrl

def delete(poolName=None, projectName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}"
    method = "POST"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(poolName=None, projectName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}"
    method = "GET"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(projectName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(projectName=None, zone=None, maxResults=None, pageToken=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools"
    method = "GET"
    return Request(
        method, 
        url.format(['projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resize(poolName=None, projectName=None, zone=None, numReplicas=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}/resize"
    method = "POST"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updatetemplate(poolName=None, projectName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}/updateTemplate"
    method = "POST"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
