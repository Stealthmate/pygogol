from pygogol.core import Request

from Defs import baseUrl

def list(accountId=None):
    url = baseUrl + "publisher/{accountId}/profiles"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
