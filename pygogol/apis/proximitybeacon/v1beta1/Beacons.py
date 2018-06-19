from pygogol.core import Request

from Defs import baseUrl

def activate(beaconName=None, projectId=None):
    url = baseUrl + "v1beta1/{+beaconName}:activate"
    method = "POST"
    return Request(
        method, 
        url.format(['beaconName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deactivate(beaconName=None, projectId=None):
    url = baseUrl + "v1beta1/{+beaconName}:deactivate"
    method = "POST"
    return Request(
        method, 
        url.format(['beaconName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def decommission(beaconName=None, projectId=None):
    url = baseUrl + "v1beta1/{+beaconName}:decommission"
    method = "POST"
    return Request(
        method, 
        url.format(['beaconName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(beaconName=None, projectId=None):
    url = baseUrl + "v1beta1/{+beaconName}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['beaconName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(beaconName=None, projectId=None):
    url = baseUrl + "v1beta1/{+beaconName}"
    method = "GET"
    return Request(
        method, 
        url.format(['beaconName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(pageSize=None, pageToken=None, projectId=None, q=None):
    url = baseUrl + "v1beta1/beacons"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def register(projectId=None):
    url = baseUrl + "v1beta1/beacons:register"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(beaconName=None, projectId=None):
    url = baseUrl + "v1beta1/{+beaconName}"
    method = "PUT"
    return Request(
        method, 
        url.format(['beaconName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
