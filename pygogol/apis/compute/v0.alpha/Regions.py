from pygogol.core import Request

from Defs import baseUrl

def get(project=None, region=None):
    url = baseUrl + "{project}/regions/{region}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
