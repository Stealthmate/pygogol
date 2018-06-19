from pygogol.core import Request

from Defs import baseUrl

def action(customerId=None, resourceId=None):
    url = baseUrl + "customer/{customerId}/devices/mobile/{resourceId}/action"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(customerId=None, resourceId=None):
    url = baseUrl + "customer/{customerId}/devices/mobile/{resourceId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customerId', 'resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customerId=None, resourceId=None, projection=None):
    url = baseUrl + "customer/{customerId}/devices/mobile/{resourceId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId', 'resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerId=None, maxResults=None, orderBy=None, pageToken=None, projection=None, query=None, sortOrder=None):
    url = baseUrl + "customer/{customerId}/devices/mobile"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
