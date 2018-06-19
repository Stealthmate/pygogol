from pygogol.core import Request

from Defs import baseUrl

def delete(compositeType=None, project=None):
    url = baseUrl + "{project}/global/compositeTypes/{compositeType}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['compositeType', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(compositeType=None, project=None):
    url = baseUrl + "{project}/global/compositeTypes/{compositeType}"
    method = "GET"
    return Request(
        method, 
        url.format(['compositeType', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "{project}/global/compositeTypes"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/compositeTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(compositeType=None, project=None):
    url = baseUrl + "{project}/global/compositeTypes/{compositeType}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['compositeType', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(compositeType=None, project=None):
    url = baseUrl + "{project}/global/compositeTypes/{compositeType}"
    method = "PUT"
    return Request(
        method, 
        url.format(['compositeType', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
