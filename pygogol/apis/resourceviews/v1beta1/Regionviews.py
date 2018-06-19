from pygogol.core import Request

from Defs import baseUrl

def addresources(projectName=None, region=None, resourceViewName=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews/{resourceViewName}/addResources"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'region', 'resourceViewName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(projectName=None, region=None, resourceViewName=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews/{resourceViewName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['projectName', 'region', 'resourceViewName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(projectName=None, region=None, resourceViewName=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews/{resourceViewName}"
    method = "GET"
    return Request(
        method, 
        url.format(['projectName', 'region', 'resourceViewName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(projectName=None, region=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(projectName=None, region=None, maxResults=None, pageToken=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews"
    method = "GET"
    return Request(
        method, 
        url.format(['projectName', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listresources(projectName=None, region=None, resourceViewName=None, maxResults=None, pageToken=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews/{resourceViewName}/resources"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'region', 'resourceViewName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeresources(projectName=None, region=None, resourceViewName=None):
    url = baseUrl + "{projectName}/regions/{region}/resourceViews/{resourceViewName}/removeResources"
    method = "POST"
    return Request(
        method, 
        url.format(['projectName', 'region', 'resourceViewName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
