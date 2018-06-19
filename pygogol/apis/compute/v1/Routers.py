from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/routers"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, region=None, router=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/routers/{router}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'router']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, router=None):
    url = baseUrl + "{project}/regions/{region}/routers/{router}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'router']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getRouterStatus(project=None, region=None, router=None):
    url = baseUrl + "{project}/regions/{region}/routers/{router}/getRouterStatus"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'router']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/routers"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/routers"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, region=None, router=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/routers/{router}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'region', 'router']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def preview(project=None, region=None, router=None):
    url = baseUrl + "{project}/regions/{region}/routers/{router}/preview"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'router']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, region=None, router=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/routers/{router}"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'region', 'router']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
