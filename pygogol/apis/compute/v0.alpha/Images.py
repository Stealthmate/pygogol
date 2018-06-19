from pygogol.core import Request

from Defs import baseUrl

def delete(image=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/images/{image}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['image', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deprecate(image=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/images/{image}/deprecate"
    method = "POST"
    return Request(
        method, 
        url.format(['image', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(image=None, project=None):
    url = baseUrl + "{project}/global/images/{image}"
    method = "GET"
    return Request(
        method, 
        url.format(['image', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getFromFamily(family=None, project=None):
    url = baseUrl + "{project}/global/images/family/{family}"
    method = "GET"
    return Request(
        method, 
        url.format(['family', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/images/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, forceCreate=None, requestId=None):
    url = baseUrl + "{project}/global/images"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/images"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/images/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(project=None, resource=None):
    url = baseUrl + "{project}/global/images/{resource}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/images/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
