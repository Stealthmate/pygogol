from pygogol.core import Request

from Defs import baseUrl

def delete(instance=None, project=None, host=None, name=None):
    url = baseUrl + "projects/{project}/instances/{instance}/users"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/users"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/users"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(instance=None, project=None, host=None, name=None):
    url = baseUrl + "projects/{project}/instances/{instance}/users"
    method = "PUT"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
