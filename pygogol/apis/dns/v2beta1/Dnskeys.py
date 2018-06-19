from pygogol.core import Request

from Defs import baseUrl

def get(dnsKeyId=None, managedZone=None, project=None, clientOperationId=None, digestType=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}"
    method = "GET"
    return Request(
        method, 
        url.format(['dnsKeyId', 'managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(managedZone=None, project=None, digestType=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/dnsKeys"
    method = "GET"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
