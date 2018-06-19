from pygogol.core import Request

from Defs import baseUrl

def delete(enterpriseId=None, managedConfigurationForUserId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId', 'managedConfigurationForUserId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(enterpriseId=None, managedConfigurationForUserId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'managedConfigurationForUserId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(enterpriseId=None, managedConfigurationForUserId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['enterpriseId', 'managedConfigurationForUserId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(enterpriseId=None, managedConfigurationForUserId=None, userId=None):
    url = baseUrl + "enterprises/{enterpriseId}/users/{userId}/managedConfigurationsForUser/{managedConfigurationForUserId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId', 'managedConfigurationForUserId', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
