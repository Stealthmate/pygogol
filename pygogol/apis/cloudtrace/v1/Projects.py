from pygogol.core import Request

from Defs import baseUrl

def patchTraces(projectId=None):
    url = baseUrl + "v1/projects/{projectId}/traces"
    method = "PATCH"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
