from pygogol.core import Request

from Defs import baseUrl

def query(siteUrl=None):
    url = baseUrl + "sites/{siteUrl}/searchAnalytics/query"
    method = "POST"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
