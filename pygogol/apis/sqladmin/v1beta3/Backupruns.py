from pygogol.core import Request

from Defs import baseUrl

def get(backupConfiguration=None, instance=None, project=None, dueTime=None):
    url = baseUrl + "projects/{project}/instances/{instance}/backupRuns/{backupConfiguration}"
    method = "GET"
    return Request(
        method, 
        url.format(['backupConfiguration', 'instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(instance=None, project=None, backupConfiguration=None, maxResults=None, pageToken=None):
    url = baseUrl + "projects/{project}/instances/{instance}/backupRuns"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
