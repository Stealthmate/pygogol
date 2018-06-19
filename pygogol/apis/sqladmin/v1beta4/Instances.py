from pygogol.core import Request

from Defs import baseUrl

def addServerCa(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/addServerCa"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def clone(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/clone"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
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

def demoteMaster(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/demoteMaster"
    method = "POST"
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

def failover(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/failover"
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

def list(project=None, filter=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{project}/instances"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listServerCas(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/listServerCas"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
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

def restoreBackup(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/restoreBackup"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rotateServerCa(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/rotateServerCa"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def startReplica(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/startReplica"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def stopReplica(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/stopReplica"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def truncateLog(instance=None, project=None):
    url = baseUrl + "projects/{project}/instances/{instance}/truncateLog"
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
