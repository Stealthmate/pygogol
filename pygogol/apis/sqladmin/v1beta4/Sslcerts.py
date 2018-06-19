from pygogol.core import Request

from Defs import baseUrl

def createEphemeral(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/createEphemeral"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instance=None, project=None, sha1Fingerprint=None):
    url = baseUrl + "projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instance', 'project', 'sha1Fingerprint']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instance=None, project=None, sha1Fingerprint=None):
    url = baseUrl + "projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project', 'sha1Fingerprint']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/sslCerts"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/sslCerts"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
