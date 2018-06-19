from pygogol.core import Request

from Defs import baseUrl

def delete(deviceId=None, enterpriseId=None, installId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'installId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(deviceId=None, enterpriseId=None, installId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}"
    method = "GET"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'installId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(deviceId=None, enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs"
    method = "GET"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(deviceId=None, enterpriseId=None, installId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'installId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(deviceId=None, enterpriseId=None, installId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/installs/{installId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'installId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
