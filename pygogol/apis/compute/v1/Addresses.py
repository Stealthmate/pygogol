from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/addresses"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(address=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/addresses/{address}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['address', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(address=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/addresses/{address}"
    method = "GET"
    return Request(
        method, 
        url.format(['address', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/addresses"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/addresses"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
