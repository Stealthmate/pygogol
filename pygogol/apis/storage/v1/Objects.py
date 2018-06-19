from pygogol.core import Request

from Defs import baseUrl

def compose(destinationBucket=None, destinationObject=None, destinationPredefinedAcl=None, ifGenerationMatch=None, ifMetagenerationMatch=None, kmsKeyName=None, userProject=None):
    url = baseUrl + "b/{destinationBucket}/o/{destinationObject}/compose"
    method = "POST"
    return Request(
        method, 
        url.format(['destinationBucket', 'destinationObject']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def copy(destinationBucket=None, destinationObject=None, sourceBucket=None, sourceObject=None, destinationPredefinedAcl=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, ifSourceGenerationMatch=None, ifSourceGenerationNotMatch=None, ifSourceMetagenerationMatch=None, ifSourceMetagenerationNotMatch=None, projection=None, sourceGeneration=None, userProject=None):
    url = baseUrl + "b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject}"
    method = "POST"
    return Request(
        method, 
        url.format(['destinationBucket', 'destinationObject', 'sourceBucket', 'sourceObject']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(bucket=None, object=None, generation=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(bucket=None, object=None, generation=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getIamPolicy(bucket=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/iam"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(bucket=None, contentEncoding=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, kmsKeyName=None, name=None, predefinedAcl=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}/o"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(bucket=None, delimiter=None, includeTrailingDelimiter=None, maxResults=None, pageToken=None, prefix=None, projection=None, userProject=None, versions=None):
    url = baseUrl + "b/{bucket}/o"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(bucket=None, object=None, generation=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, predefinedAcl=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rewrite(destinationBucket=None, destinationObject=None, sourceBucket=None, sourceObject=None, destinationKmsKeyName=None, destinationPredefinedAcl=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, ifSourceGenerationMatch=None, ifSourceGenerationNotMatch=None, ifSourceMetagenerationMatch=None, ifSourceMetagenerationNotMatch=None, maxBytesRewrittenPerCall=None, projection=None, rewriteToken=None, sourceGeneration=None, userProject=None):
    url = baseUrl + "b/{sourceBucket}/o/{sourceObject}/rewriteTo/b/{destinationBucket}/o/{destinationObject}"
    method = "POST"
    return Request(
        method, 
        url.format(['destinationBucket', 'destinationObject', 'sourceBucket', 'sourceObject']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setIamPolicy(bucket=None, object=None, generation=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/iam"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(bucket=None, object=None, generation=None, permissions=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}/iam/testPermissions"
    method = "GET"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(bucket=None, object=None, generation=None, ifGenerationMatch=None, ifGenerationNotMatch=None, ifMetagenerationMatch=None, ifMetagenerationNotMatch=None, predefinedAcl=None, projection=None, userProject=None):
    url = baseUrl + "b/{bucket}/o/{object}"
    method = "PUT"
    return Request(
        method, 
        url.format(['bucket', 'object']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watchAll(bucket=None, delimiter=None, includeTrailingDelimiter=None, maxResults=None, pageToken=None, prefix=None, projection=None, userProject=None, versions=None):
    url = baseUrl + "b/{bucket}/o/watch"
    method = "POST"
    return Request(
        method, 
        url.format(['bucket']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
