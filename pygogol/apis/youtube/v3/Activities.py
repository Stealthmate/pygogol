from pygogol.core import Request

from Defs import baseUrl

def insert(part=None):
    url = baseUrl + "activities"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(channelId=None, home=None, maxResults=None, mine=None, pageToken=None, part=None, publishedAfter=None, publishedBefore=None, regionCode=None):
    url = baseUrl + "activities"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
