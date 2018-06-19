from pygogol.core import Request

from Defs import baseUrl

def getLinkStats(dynamicLink=None, durationDays=None):
    url = baseUrl + "v1/{dynamicLink}/linkStats"
    method = "GET"
    return Request(
        method, 
        url.format(['dynamicLink']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def installAttribution():
    url = baseUrl + "v1/installAttribution"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
