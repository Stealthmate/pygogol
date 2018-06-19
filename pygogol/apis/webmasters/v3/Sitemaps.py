from pygogol.core import Request

from Defs import baseUrl

def delete(feedpath=None, siteUrl=None):
    url = baseUrl + "sites/{siteUrl}/sitemaps/{feedpath}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['feedpath', 'siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(feedpath=None, siteUrl=None):
    url = baseUrl + "sites/{siteUrl}/sitemaps/{feedpath}"
    method = "GET"
    return Request(
        method, 
        url.format(['feedpath', 'siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(siteUrl=None, sitemapIndex=None):
    url = baseUrl + "sites/{siteUrl}/sitemaps"
    method = "GET"
    return Request(
        method, 
        url.format(['siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def submit(feedpath=None, siteUrl=None):
    url = baseUrl + "sites/{siteUrl}/sitemaps/{feedpath}"
    method = "PUT"
    return Request(
        method, 
        url.format(['feedpath', 'siteUrl']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
