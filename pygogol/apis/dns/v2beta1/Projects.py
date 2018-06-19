from pygogol.core import Request

from Defs import baseUrl

def get(project=None, clientOperationId=None):
    url = baseUrl + "{project}"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
