from pygogol.core import Request

from Defs import baseUrl

def delete(interconnect=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/interconnects/{interconnect}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['interconnect', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(interconnect=None, project=None):
    url = baseUrl + "{project}/global/interconnects/{interconnect}"
    method = "GET"
    return Request(
        method, 
        url.format(['interconnect', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/interconnects"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/interconnects"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(interconnect=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/interconnects/{interconnect}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['interconnect', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
