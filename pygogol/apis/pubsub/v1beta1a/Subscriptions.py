from pygogol.core import Request

from Defs import baseUrl

def acknowledge():
    url = baseUrl + "v1beta1a/subscriptions/acknowledge"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create():
    url = baseUrl + "v1beta1a/subscriptions"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(subscription=None):
    url = baseUrl + "v1beta1a/subscriptions/{+subscription}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['subscription']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(subscription=None):
    url = baseUrl + "v1beta1a/subscriptions/{+subscription}"
    method = "GET"
    return Request(
        method, 
        url.format(['subscription']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None, query=None):
    url = baseUrl + "v1beta1a/subscriptions"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def modifyAckDeadline():
    url = baseUrl + "v1beta1a/subscriptions/modifyAckDeadline"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def modifyPushConfig():
    url = baseUrl + "v1beta1a/subscriptions/modifyPushConfig"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def pull():
    url = baseUrl + "v1beta1a/subscriptions/pull"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def pullBatch():
    url = baseUrl + "v1beta1a/subscriptions/pullBatch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
