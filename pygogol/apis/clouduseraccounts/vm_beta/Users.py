from pygogol.core import Request

from Defs import baseUrl

def addPublicKey(project=None, user=None):
    url = baseUrl + "{project}/global/users/{user}/addPublicKey"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'user']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(project=None, user=None):
    url = baseUrl + "{project}/global/users/{user}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'user']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, user=None):
    url = baseUrl + "{project}/global/users/{user}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'user']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "{project}/global/users"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/users"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def removePublicKey(project=None, user=None, fingerprint=None):
    url = baseUrl + "{project}/global/users/{user}/removePublicKey"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'user']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
