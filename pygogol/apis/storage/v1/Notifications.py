from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, notification=None, userProject=None):
    url = baseUrl + "b/{bucket}/notificationConfigs/{notification}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket', 'notification']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, notification=None, userProject=None):
    url = baseUrl + "b/{bucket}/notificationConfigs/{notification}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'notification']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(bucket=None, userProject=None):
    url = baseUrl + "b/{bucket}/notificationConfigs"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bucket=None, userProject=None):
    url = baseUrl + "b/{bucket}/notificationConfigs"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
