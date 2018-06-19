from pygogol.core import Request

from Defs import baseUrl

def get(projectId=None):
    url = baseUrl + "v1/googleServiceAccounts/{projectId}"
    method = "GET"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
