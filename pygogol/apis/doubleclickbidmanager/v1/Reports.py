from pygogol.core import Request

from Defs import baseUrl

def listreports(queryId=None):
    url = baseUrl + "queries/{queryId}/reports"
    method = "GET"
    return Request(
        method, 
        url.format(['queryId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
