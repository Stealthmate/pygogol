from pygogol.core import Request

from Defs import baseUrl

def get(proposalId=None):
    url = baseUrl + "proposals/{proposalId}"
    method = "GET"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "proposals/insert"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(proposalId=None, revisionNumber=None, updateAction=None):
    url = baseUrl + "proposals/{proposalId}/{revisionNumber}/{updateAction}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['proposalId', 'revisionNumber', 'updateAction']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search(pqlQuery=None):
    url = baseUrl + "proposals/search"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setupcomplete(proposalId=None):
    url = baseUrl + "proposals/{proposalId}/setupcomplete"
    method = "POST"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(proposalId=None, revisionNumber=None, updateAction=None):
    url = baseUrl + "proposals/{proposalId}/{revisionNumber}/{updateAction}"
    method = "PUT"
    return Request(
        method, 
        url.format(['proposalId', 'revisionNumber', 'updateAction']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
