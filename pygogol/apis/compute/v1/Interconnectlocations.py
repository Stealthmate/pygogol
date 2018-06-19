from pygogol.core import Request

from Defs import baseUrl

def get(interconnectLocation=None, project=None):
    url = baseUrl + "{project}/global/interconnectLocations/{interconnectLocation}"
    method = "GET"
    return Request(
        method, 
        url.format(['interconnectLocation', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/interconnectLocations"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
