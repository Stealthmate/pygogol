from pygogol.core import Request

from Defs import baseUrl

def representativeInfoByAddress(address=None, includeOffices=None, levels=None, roles=None):
    url = baseUrl + "representatives"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def representativeInfoByDivision(ocdId=None, levels=None, recursive=None, roles=None):
    url = baseUrl + "representatives/{ocdId}"
    method = "GET"
    return Request(
        method, 
        url.format(['ocdId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
