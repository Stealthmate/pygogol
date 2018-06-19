from pygogol.core import Request

from Defs import baseUrl

def download(resourceName=None):
    url = baseUrl + "v1/media/{+resourceName}"
    method = "GET"
    return Request(
        method, 
        url.format(['resourceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
