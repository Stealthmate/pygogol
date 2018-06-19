from pygogol.core import Request

from Defs import baseUrl

def list(hl=None, part=None):
    url = baseUrl + "videoAbuseReportReasons"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
