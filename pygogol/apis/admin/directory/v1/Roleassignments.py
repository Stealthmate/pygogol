from pygogol.core import Request

from Defs import baseUrl

def delete(customer=None, roleAssignmentId=None):
    url = baseUrl + "customer/{customer}/roleassignments/{roleAssignmentId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customer', 'roleAssignmentId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customer=None, roleAssignmentId=None):
    url = baseUrl + "customer/{customer}/roleassignments/{roleAssignmentId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customer', 'roleAssignmentId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customer=None):
    url = baseUrl + "customer/{customer}/roleassignments"
    method = "POST"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customer=None, maxResults=None, pageToken=None, roleId=None, userKey=None):
    url = baseUrl + "customer/{customer}/roleassignments"
    method = "GET"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
