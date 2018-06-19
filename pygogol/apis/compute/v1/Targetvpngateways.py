from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/targetVpnGateways"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, region=None, targetVpnGateway=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetVpnGateways/{targetVpnGateway}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'targetVpnGateway']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, targetVpnGateway=None):
    url = baseUrl + "{project}/regions/{region}/targetVpnGateways/{targetVpnGateway}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'targetVpnGateway']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/targetVpnGateways"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/targetVpnGateways"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
