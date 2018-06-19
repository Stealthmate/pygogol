from pygogol.core import Request

from Defs import baseUrl

def listOfflineMetadata(cpksver=None):
    url = baseUrl + "dictionary/listOfflineMetadata"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
