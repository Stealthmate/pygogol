from pygogol.core import Request

from Defs import baseUrl

def run(scriptId=None):
    url = baseUrl + "v1/scripts/{scriptId}:run"
    method = "POST"
    return Request(
        method, 
        url.format(['scriptId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
