from pygogol.core import Request

from Defs import baseUrl

def addresources(projectName=None, resourceViewName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews/{resourceViewName}/addResources"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'resourceViewName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(projectName=None, resourceViewName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews/{resourceViewName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['projectName', 'resourceViewName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(projectName=None, resourceViewName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews/{resourceViewName}"
    method = "GET"
    return Request(
        method, 
        url.format(['projectName', 'resourceViewName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(projectName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(projectName=None, zone=None, maxResults=None, pageToken=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews"
    method = "GET"
    return Request(
        method, 
        url.format(['projectName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listresources(projectName=None, resourceViewName=None, zone=None, maxResults=None, pageToken=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews/{resourceViewName}/resources"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'resourceViewName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeresources(projectName=None, resourceViewName=None, zone=None):
    url = baseUrl + "{projectName}/zones/{zone}/resourceViews/{resourceViewName}/removeResources"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'resourceViewName', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
