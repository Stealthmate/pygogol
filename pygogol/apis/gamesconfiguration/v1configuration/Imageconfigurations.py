from pygogol.core import Request

from Defs import baseUrl

def upload(imageType=None, resourceId=None):
    url = baseUrl + "images/{resourceId}/imageType/{imageType}"
    method = "POST"
    return Request(
        method, 
        url.format(['imageType', 'resourceId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
