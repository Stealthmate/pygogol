from pygogol.core import Request

from Defs import baseUrl

def addResources(project=None, resourceView=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}/addResources"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, resourceView=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, resourceView=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getService(project=None, resourceView=None, zone=None, resourceName=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}/getService"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listResources(project=None, resourceView=None, zone=None, format=None, listState=None, maxResults=None, pageToken=None, serviceName=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}/resources"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeResources(project=None, resourceView=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}/removeResources"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setService(project=None, resourceView=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/resourceViews/{resourceView}/setService"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resourceView', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
