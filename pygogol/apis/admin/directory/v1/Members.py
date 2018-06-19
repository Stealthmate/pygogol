from pygogol.core import Request

from Defs import baseUrl

def delete(groupKey=None, memberKey=None):
    url = baseUrl + "groups/{groupKey}/members/{memberKey}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['groupKey', 'memberKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(groupKey=None, memberKey=None):
    url = baseUrl + "groups/{groupKey}/members/{memberKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['groupKey', 'memberKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def hasMember(groupKey=None, memberKey=None):
    url = baseUrl + "groups/{groupKey}/hasMember/{memberKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['groupKey', 'memberKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(groupKey=None):
    url = baseUrl + "groups/{groupKey}/members"
    method = "POST"
    return Request(
        method, 
        url.format(['groupKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(groupKey=None, includeDerivedMembership=None, maxResults=None, pageToken=None, roles=None):
    url = baseUrl + "groups/{groupKey}/members"
    method = "GET"
    return Request(
        method, 
        url.format(['groupKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(groupKey=None, memberKey=None):
    url = baseUrl + "groups/{groupKey}/members/{memberKey}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['groupKey', 'memberKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(groupKey=None, memberKey=None):
    url = baseUrl + "groups/{groupKey}/members/{memberKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['groupKey', 'memberKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
