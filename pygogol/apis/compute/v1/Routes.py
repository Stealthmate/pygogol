from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, route=None, requestId=None):
    url = baseUrl + "{project}/global/routes/{route}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'route']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, route=None):
    url = baseUrl + "{project}/global/routes/{route}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'route']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/routes"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/routes"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
