from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/diskTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(diskType=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/diskTypes/{diskType}"
    method = "GET"
    return Request(
        method, 
        url.format(['diskType', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/diskTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
