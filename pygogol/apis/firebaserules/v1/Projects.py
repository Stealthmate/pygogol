from pygogol.core import Request

from Defs import baseUrl

def test(name=None):
    url = baseUrl + "v1/{+name}:test"
    method = "POST"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
