from pygogol.core import Request

from Defs import baseUrl

def delete(license=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/licenses/{license}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['license', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(license=None, project=None):
    url = baseUrl + "{project}/global/licenses/{license}"
    method = "GET"
    return Request(
        method, 
        url.format(['license', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/licenses"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/licenses"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
