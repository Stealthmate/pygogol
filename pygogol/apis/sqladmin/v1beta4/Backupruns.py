from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/backupRuns/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None, instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/backupRuns/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/backupRuns"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(instance=None, project=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{project}/instances/{instance}/backupRuns"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
