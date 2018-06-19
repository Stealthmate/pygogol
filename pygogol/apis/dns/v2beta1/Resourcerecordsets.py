from pygogol.core import Request

from Defs import baseUrl

def list(managedZone=None, project=None, maxResults=None, name=None, pageToken=None, type=None):
    url = baseUrl + "{project}/managedZones/{managedZone}/rrsets"
    method = "GET"
    return Request(
        method, 
        url.format(['managedZone', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
