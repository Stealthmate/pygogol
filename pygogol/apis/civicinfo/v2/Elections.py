from pygogol.core import Request

from Defs import baseUrl

def electionQuery():
    url = baseUrl + "elections"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def voterInfoQuery(address=None, electionId=None, officialOnly=None, returnAllAvailableData=None):
    url = baseUrl + "voterinfo"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
