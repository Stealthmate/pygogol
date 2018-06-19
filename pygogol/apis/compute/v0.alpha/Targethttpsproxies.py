from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, targetHttpsProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetHttpsProxies/{targetHttpsProxy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'targetHttpsProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, targetHttpsProxy=None):
    url = baseUrl + "{project}/global/targetHttpsProxies/{targetHttpsProxy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'targetHttpsProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/targetHttpsProxies"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/targetHttpsProxies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setQuicOverride(project=None, targetHttpsProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetHttpsProxies/{targetHttpsProxy}/setQuicOverride"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetHttpsProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setSslCertificates(project=None, targetHttpsProxy=None, requestId=None):
    url = baseUrl + "{project}/targetHttpsProxies/{targetHttpsProxy}/setSslCertificates"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetHttpsProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setSslPolicy(project=None, targetHttpsProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetHttpsProxies/{targetHttpsProxy}/setSslPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetHttpsProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setUrlMap(project=None, targetHttpsProxy=None, requestId=None):
    url = baseUrl + "{project}/targetHttpsProxies/{targetHttpsProxy}/setUrlMap"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetHttpsProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/targetHttpsProxies/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
