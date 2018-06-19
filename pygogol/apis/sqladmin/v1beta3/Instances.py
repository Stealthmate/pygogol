from pygogol.core import Request

from Defs import baseUrl

def clone(project=None):
    url = baseUrl + "projects/{project}/instances/clone"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def export(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/export"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def import(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/import"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "projects/{project}/instances"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{project}/instances"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def promoteReplica(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/promoteReplica"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetSslConfig(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/resetSslConfig"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def restart(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/restart"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def restoreBackup(instance=None, project=None, backupConfiguration=None, dueTime=None):
    url = baseUrl + "projects/{project}/instances/{instance}/restoreBackup"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setRootPassword(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/setRootPassword"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}"
    method = "PUT"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
