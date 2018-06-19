from pygogol.core import Request

from Defs import baseUrl

def delete(enterpriseId=None, entitlementId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'entitlementId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(enterpriseId=None, entitlementId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'entitlementId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/entitlements"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(enterpriseId=None, entitlementId=None, userId=None, install=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['enterpriseId', 'entitlementId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(enterpriseId=None, entitlementId=None, userId=None, install=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/entitlements/{entitlementId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId', 'entitlementId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
