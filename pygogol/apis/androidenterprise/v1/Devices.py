from pygogol.core import Request

from Defs import baseUrl

def get(deviceId=None, enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}"
    method = "GET"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getState(deviceId=None, enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/state"
    method = "GET"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(deviceId=None, enterpriseId=None, userId=None, updateMask=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setState(deviceId=None, enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/state"
    method = "PUT"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(deviceId=None, enterpriseId=None, userId=None, updateMask=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
