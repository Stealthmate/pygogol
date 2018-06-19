from pygogol.core import Request

from Defs import baseUrl

def action(customerId=None, resourceId=None):
    url = baseUrl + "customer/{customerId}/devices/chromeos/{resourceId}/action"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customerId=None, deviceId=None, projection=None):
    url = baseUrl + "customer/{customerId}/devices/chromeos/{deviceId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId', 'deviceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerId=None, maxResults=None, orderBy=None, orgUnitPath=None, pageToken=None, projection=None, query=None, sortOrder=None):
    url = baseUrl + "customer/{customerId}/devices/chromeos"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def moveDevicesToOu(customerId=None, orgUnitPath=None):
    url = baseUrl + "customer/{customerId}/devices/chromeos/moveDevicesToOu"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customerId=None, deviceId=None, projection=None):
    url = baseUrl + "customer/{customerId}/devices/chromeos/{deviceId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customerId', 'deviceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customerId=None, deviceId=None, projection=None):
    url = baseUrl + "customer/{customerId}/devices/chromeos/{deviceId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customerId', 'deviceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
