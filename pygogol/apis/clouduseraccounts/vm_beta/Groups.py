from pygogol.core import Request

from Defs import baseUrl

def addMember(groupName=None, project=None):
    url = baseUrl + "{project}/global/groups/{groupName}/addMember"
    method = "POST"
    return Request(
        method, 
        url.format(['groupName', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(groupName=None, project=None):
    url = baseUrl + "{project}/global/groups/{groupName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['groupName', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(groupName=None, project=None):
    url = baseUrl + "{project}/global/groups/{groupName}"
    method = "GET"
    return Request(
        method, 
        url.format(['groupName', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "{project}/global/groups"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/groups"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removeMember(groupName=None, project=None):
    url = baseUrl + "{project}/global/groups/{groupName}/removeMember"
    method = "POST"
    return Request(
        method, 
        url.format(['groupName', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
