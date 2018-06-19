from pygogol.core import Request

from Defs import baseUrl

def delete(customer=None, notificationId=None):
    url = baseUrl + "customer/{customer}/notifications/{notificationId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customer', 'notificationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customer=None, notificationId=None):
    url = baseUrl + "customer/{customer}/notifications/{notificationId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customer', 'notificationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customer=None, language=None, maxResults=None, pageToken=None):
    url = baseUrl + "customer/{customer}/notifications"
    method = "GET"
    return Request(
        method, 
        url.format(['customer']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(customer=None, notificationId=None):
    url = baseUrl + "customer/{customer}/notifications/{notificationId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['customer', 'notificationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(customer=None, notificationId=None):
    url = baseUrl + "customer/{customer}/notifications/{notificationId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['customer', 'notificationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
