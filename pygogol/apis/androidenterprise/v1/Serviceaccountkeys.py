from pygogol.core import Request

from Defs import baseUrl

def delete(enterpriseId=None, keyId=None):
    url = baseUrl + "enterprises/{enterpriseId}/serviceAccountKeys/{keyId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'keyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/serviceAccountKeys"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/serviceAccountKeys"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
