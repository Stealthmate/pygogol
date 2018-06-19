from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, sslCertificate=None, requestId=None):
    url = baseUrl + "{project}/global/sslCertificates/{sslCertificate}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'sslCertificate']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, sslCertificate=None):
    url = baseUrl + "{project}/global/sslCertificates/{sslCertificate}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'sslCertificate']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/sslCertificates"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/sslCertificates"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None):
    url = baseUrl + "{project}/global/sslCertificates/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
