from pygogol.core import Request

from Defs import baseUrl

def list(project=None):
    url = baseUrl + "projects/{project}/tiers"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
