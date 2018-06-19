from pygogol.core import Request

from Defs import baseUrl

def get(accountId=None):
    url = baseUrl + "accounts/{accountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['accountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
