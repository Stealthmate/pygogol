from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/targetInstances"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, targetInstance=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/targetInstances/{targetInstance}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'targetInstance', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, targetInstance=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/targetInstances/{targetInstance}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'targetInstance', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/targetInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/targetInstances"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
