from pygogol.core import Request

from Defs import baseUrl

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/machineTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(machineType=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/machineTypes/{machineType}"
    method = "GET"
    return Request(
        method, 
        url.format(['machineType', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/machineTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
