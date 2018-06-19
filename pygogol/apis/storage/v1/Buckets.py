from pygogol.core import Request

from Defs import baseUrl

def delete(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, userProject=None):
    url = baseUrl + "b/{bucket}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(bucket=None, userProject=None):
    url = baseUrl + "b/{bucket}/iam"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(predefinedAcl=None, predefinedDefaultObjectAcl=None, project=None, projection=None, userProject=None):
    url = baseUrl + "b"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None, prefix=None, project=None, projection=None, userProject=None):
    url = baseUrl + "b"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def lockRetentionPolicy(bucket=None, ifMetagenerationMatch=None, userProject=None):
    url = baseUrl + "b/{bucket}/lockRetentionPolicy"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, predefinedAcl=None, predefinedDefaultObjectAcl=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(bucket=None, userProject=None):
    url = baseUrl + "b/{bucket}/iam"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(bucket=None, permissions=None, userProject=None):
    url = baseUrl + "b/{bucket}/iam/testPermissions"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, predefinedAcl=None, predefinedDefaultObjectAcl=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
