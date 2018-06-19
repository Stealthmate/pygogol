from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, targetTcpProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetTcpProxies/{targetTcpProxy}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'targetTcpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, targetTcpProxy=None):
    url = baseUrl + "{project}/global/targetTcpProxies/{targetTcpProxy}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'targetTcpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/targetTcpProxies"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/targetTcpProxies"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setBackendService(project=None, targetTcpProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetTcpProxies/{targetTcpProxy}/setBackendService"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetTcpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setProxyHeader(project=None, targetTcpProxy=None, requestId=None):
    url = baseUrl + "{project}/global/targetTcpProxies/{targetTcpProxy}/setProxyHeader"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'targetTcpProxy']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
