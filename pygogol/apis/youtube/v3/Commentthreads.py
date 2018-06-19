from pygogol.core import Request

from Defs import baseUrl

def insert(part=None):
    url = baseUrl + "commentThreads"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(allThreadsRelatedToChannelId=None, channelId=None, id=None, maxResults=None, moderationStatus=None, order=None, pageToken=None, part=None, searchTerms=None, textFormat=None, videoId=None):
    url = baseUrl + "commentThreads"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(part=None):
    url = baseUrl + "commentThreads"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
