from pygogol.core import Request

from Defs import baseUrl

def query(siteUrl=None, category=None, latestCountsOnly=None, platform=None):
    url = baseUrl + "sites/{siteUrl}/urlCrawlErrorsCounts/query"
    method = "GET"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
