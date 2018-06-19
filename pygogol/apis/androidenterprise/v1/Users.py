from pygogol.core import Request

from Defs import baseUrl

def delete(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generateAuthenticationToken(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/authenticationToken"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generateToken(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/token"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getAvailableProductSet(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/availableProductSet"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None, email=None):
    url = baseUrl + "enterprises/{enterpriseId}/users"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def revokeDeviceAccess(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/deviceAccess"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def revokeToken(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/token"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setAvailableProductSet(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/availableProductSet"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
