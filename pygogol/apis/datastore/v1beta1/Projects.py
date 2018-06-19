from pygogol.core import Request

from Defs import baseUrl

def export(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}:export"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def import(projectId=None):
    url = baseUrl + "v1beta1/projects/{projectId}:import"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
