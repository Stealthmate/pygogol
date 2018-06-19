from pygogol.core import Request

from Defs import baseUrl

def delete(poolName=None, projectName=None, replicaName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName}"
    method = "POST"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'replicaName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(poolName=None, projectName=None, replicaName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName}"
    method = "GET"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'replicaName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(poolName=None, projectName=None, zone=None, maxResults=None, pageToken=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}/replicas"
    method = "GET"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def restart(poolName=None, projectName=None, replicaName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName}/restart"
    method = "POST"
    return Request(
        method, 
        url.format(['poolName', 'projectName', 'replicaName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
