from pygogol.core import Request

from Defs import baseUrl

def delete(instanceTemplate=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/instanceTemplates/{instanceTemplate}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instanceTemplate', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instanceTemplate=None, project=None):
    url = baseUrl + "{project}/global/instanceTemplates/{instanceTemplate}"
    method = "GET"
    return Request(
        method, 
        url.format(['instanceTemplate', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/instanceTemplates"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/instanceTemplates"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/instanceTemplates/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
