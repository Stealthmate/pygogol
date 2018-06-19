from pygogol.core import Request

from Defs import baseUrl

def insert(proposalId=None):
    url = baseUrl + "proposals/{proposalId}/notes/insert"
    method = "POST"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(proposalId=None, pqlQuery=None):
    url = baseUrl + "proposals/{proposalId}/notes"
    method = "GET"
    return Request(
        method, 
        url.format(['proposalId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
