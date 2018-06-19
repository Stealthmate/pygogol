from pygogol.core import Request

from Defs import baseUrl

def insert(accountName=None, accountType=None, userToken=None):
    url = baseUrl + "accounts/{userToken}/{accountType}/{accountName}"
    method = "POST"
    return Request(
        method, 
        url.format(['accountName', 'accountType', 'userToken']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
