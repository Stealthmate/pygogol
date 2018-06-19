from pygogol.core import Request

from Defs import baseUrl

def addSignedUrlKey(backendBucket=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendBuckets/{backendBucket}/addSignedUrlKey"
    method = "POST"
    return Request(
        method, 
        url.format(['backendBucket', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(backendBucket=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendBuckets/{backendBucket}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['backendBucket', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteSignedUrlKey(backendBucket=None, project=None, keyName=None, requestId=None):
    url = baseUrl + "{project}/global/backendBuckets/{backendBucket}/deleteSignedUrlKey"
    method = "POST"
    return Request(
        method, 
        url.format(['backendBucket', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(backendBucket=None, project=None):
    url = baseUrl + "{project}/global/backendBuckets/{backendBucket}"
    method = "GET"
    return Request(
        method, 
        url.format(['backendBucket', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/backendBuckets"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/backendBuckets"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(backendBucket=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendBuckets/{backendBucket}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['backendBucket', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(backendBucket=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/backendBuckets/{backendBucket}"
    method = "PUT"
    return Request(
        method, 
        url.format(['backendBucket', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
