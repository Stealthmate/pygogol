from pygogol.core import Request

from Defs import baseUrl

def get(diskType=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/diskTypes/{diskType}"
    method = "GET"
    return Request(
        method, 
        url.format(['diskType', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/diskTypes"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
