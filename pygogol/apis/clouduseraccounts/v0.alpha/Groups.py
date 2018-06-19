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

def getIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/groups/{resource}/getIamPolicy"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
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

def setIamPolicy(project=None, resource=None):
    url = baseUrl + "{project}/global/groups/{resource}/setIamPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/groups/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
