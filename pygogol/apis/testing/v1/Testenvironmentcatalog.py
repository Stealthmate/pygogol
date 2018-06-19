from pygogol.core import Request

from Defs import baseUrl

def get(environmentType=None, projectId=None):
    url = baseUrl + "v1/testEnvironmentCatalog/{environmentType}"
    method = "GET"
    return Request(
        method, 
        url.format(['environmentType']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
