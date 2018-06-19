from pygogol.core import Request

from Defs import baseUrl

def get(locale=None, notification_id=None, source=None):
    url = baseUrl + "notification/get"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
