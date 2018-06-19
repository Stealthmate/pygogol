from pygogol.core import Request

from Defs import baseUrl

def list(channelId=None, channelType=None, eventType=None, forContentOwner=None, forDeveloper=None, forMine=None, location=None, locationRadius=None, maxResults=None, onBehalfOfContentOwner=None, order=None, pageToken=None, part=None, publishedAfter=None, publishedBefore=None, q=None, regionCode=None, relatedToVideoId=None, relevanceLanguage=None, safeSearch=None, topicId=None, type=None, videoCaption=None, videoCategoryId=None, videoDefinition=None, videoDimension=None, videoDuration=None, videoEmbeddable=None, videoLicense=None, videoSyndicated=None, videoType=None):
    url = baseUrl + "search"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
