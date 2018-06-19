from pygogol.core import Request

from Defs import baseUrl

def generate():
    url = baseUrl + "reports/generate"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(reportId=None):
    url = baseUrl + "reports/{reportId}"
    method = "GET"
    return Request(
        method, 
        url.format(['reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getFile(reportFragment=None, reportId=None):
    url = baseUrl + "reports/{reportId}/files/{reportFragment}"
    method = "GET"
    return Request(
        method, 
        url.format(['reportFragment', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def request():
    url = baseUrl + "reports"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
