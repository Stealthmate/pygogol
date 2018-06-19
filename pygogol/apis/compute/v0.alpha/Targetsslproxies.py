from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, targetSslProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetSslProxies/{targetSslProxy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'targetSslProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, targetSslProxy=None):
    url = baseUrl + "{project}/global/targetSslProxies/{targetSslProxy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'targetSslProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/targetSslProxies"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/targetSslProxies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setBackendService(project=None, targetSslProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetSslProxies/{targetSslProxy}/setBackendService"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetSslProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setProxyHeader(project=None, targetSslProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetSslProxies/{targetSslProxy}/setProxyHeader"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetSslProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setSslCertificates(project=None, targetSslProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetSslProxies/{targetSslProxy}/setSslCertificates"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetSslProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setSslPolicy(project=None, targetSslProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetSslProxies/{targetSslProxy}/setSslPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetSslProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/targetSslProxies/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
