from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, targetHttpProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetHttpProxies/{targetHttpProxy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'targetHttpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, targetHttpProxy=None):
    url = baseUrl + "{project}/global/targetHttpProxies/{targetHttpProxy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'targetHttpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/targetHttpProxies"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/targetHttpProxies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setUrlMap(project=None, targetHttpProxy=None, requestId=None):
    url = baseUrl + "{project}/targetHttpProxies/{targetHttpProxy}/setUrlMap"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetHttpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
