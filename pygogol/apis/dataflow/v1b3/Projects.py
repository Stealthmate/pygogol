from pygogol.core import Request

from Defs import baseUrl

def workerMessages(projectId=None):
    url = baseUrl + "v1b3/projects/{projectId}/WorkerMessages"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
