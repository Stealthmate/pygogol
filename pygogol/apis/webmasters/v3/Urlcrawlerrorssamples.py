from pygogol.core import Request

from Defs import baseUrl

def get(siteUrl=None, url=None, category=None, platform=None):
    url = baseUrl + "sites/{siteUrl}/urlCrawlErrorsSamples/{url}"
    method = "GET"
    return Request(
        method, 
        url.format(['siteUrl', 'url']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(siteUrl=None, category=None, platform=None):
    url = baseUrl + "sites/{siteUrl}/urlCrawlErrorsSamples"
    method = "GET"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def markAsFixed(siteUrl=None, url=None, category=None, platform=None):
    url = baseUrl + "sites/{siteUrl}/urlCrawlErrorsSamples/{url}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['siteUrl', 'url']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
