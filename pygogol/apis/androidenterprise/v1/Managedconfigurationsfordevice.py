from pygogol.core import Request

from Defs import baseUrl

def delete(deviceId=None, enterpriseId=None, managedConfigurationForDeviceId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'managedConfigurationForDeviceId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(deviceId=None, enterpriseId=None, managedConfigurationForDeviceId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}"
    method = "GET"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'managedConfigurationForDeviceId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(deviceId=None, enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice"
    method = "GET"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(deviceId=None, enterpriseId=None, managedConfigurationForDeviceId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'managedConfigurationForDeviceId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(deviceId=None, enterpriseId=None, managedConfigurationForDeviceId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/devices/{deviceId}/managedConfigurationsForDevice/{managedConfigurationForDeviceId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['deviceId', 'enterpriseId', 'managedConfigurationForDeviceId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
