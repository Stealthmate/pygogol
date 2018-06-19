from pygogol.core import Request

from Defs import baseUrl

def delete(database=None, instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/databases/{database}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['database', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(database=None, instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/databases/{database}"
    method = "GET"
    return Request(
        method, 
        url.format(['database', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/databases"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/databases"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(database=None, instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/databases/{database}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['database', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(database=None, instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/databases/{database}"
    method = "PUT"
    return Request(
        method, 
        url.format(['database', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
