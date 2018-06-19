from pygogol.core import Request

from Defs import baseUrl

def list(projectId=None):
    url = baseUrl + "v1beta1/namespaces"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(namespaceName=None, projectId=None):
    url = baseUrl + "v1beta1/{+namespaceName}"
    method = "PUT"
    return Request(
        method, 
        url.format(['namespaceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
