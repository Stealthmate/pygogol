from pygogol.core import Request

from Defs import baseUrl

def get(packageName=None, reviewId=None, translationLanguage=None):
    url = baseUrl + "{packageName}/reviews/{reviewId}"
    method = "GET"
    return Request(
        method, 
        url.format(['packageName', 'reviewId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(packageName=None, maxResults=None, startIndex=None, token=None, translationLanguage=None):
    url = baseUrl + "{packageName}/reviews"
    method = "GET"
    return Request(
        method, 
        url.format(['packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reply(packageName=None, reviewId=None):
    url = baseUrl + "{packageName}/reviews/{reviewId}:reply"
    method = "POST"
    return Request(
        method, 
        url.format(['packageName', 'reviewId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
