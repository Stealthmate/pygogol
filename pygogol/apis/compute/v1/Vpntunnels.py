from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/vpnTunnels"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, region=None, vpnTunnel=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/vpnTunnels/{vpnTunnel}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'region', 'vpnTunnel']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, region=None, vpnTunnel=None):
    url = baseUrl + "{project}/regions/{region}/vpnTunnels/{vpnTunnel}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region', 'vpnTunnel']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/vpnTunnels"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/vpnTunnels"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
