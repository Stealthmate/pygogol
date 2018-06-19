from pygogol.core import Request

from Defs import baseUrl

def delete(proposalId=None):
    url = baseUrl + "proposals/{proposalId}/deals/delete"
    method = "POST"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(proposalId=None):
    url = baseUrl + "proposals/{proposalId}/deals/insert"
    method = "POST"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(proposalId=None, pqlQuery=None):
    url = baseUrl + "proposals/{proposalId}/deals"
    method = "GET"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(proposalId=None):
    url = baseUrl + "proposals/{proposalId}/deals/update"
    method = "POST"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
