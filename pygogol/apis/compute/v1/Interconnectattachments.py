from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/interconnectAttachments"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(interconnectAttachment=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/interconnectAttachments/{interconnectAttachment}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['interconnectAttachment', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(interconnectAttachment=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/interconnectAttachments/{interconnectAttachment}"
    method = "GET"
    return Request(
        method, 
        url.format(['interconnectAttachment', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/interconnectAttachments"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/interconnectAttachments"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(interconnectAttachment=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/interconnectAttachments/{interconnectAttachment}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['interconnectAttachment', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
