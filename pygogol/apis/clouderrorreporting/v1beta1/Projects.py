from pygogol.core import Request

from Defs import baseUrl

def deleteEvents(projectName=None):
    url = baseUrl + "v1beta1/{+projectName}/events"
    method = "DELETE"
    return Request(
        method, 
        url.format(['projectName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
