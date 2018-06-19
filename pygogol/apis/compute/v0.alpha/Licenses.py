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

def getIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/licenses/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
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

def setIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/licenses/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/licenses/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
