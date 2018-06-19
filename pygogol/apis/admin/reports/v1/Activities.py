from pygogol.core import Request

from Defs import baseUrl

def list(applicationName=None, userKey=None, actorIpAddress=None, customerId=None, endTime=None, eventName=None, filters=None, maxResults=None, pageToken=None, startTime=None):
    url = baseUrl + "activity/users/{userKey}/applications/{applicationName}"
    method = "GET"
    return Request(
        method, 
        url.format(['applicationName', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(applicationName=None, userKey=None, actorIpAddress=None, customerId=None, endTime=None, eventName=None, filters=None, maxResults=None, pageToken=None, startTime=None):
    url = baseUrl + "activity/users/{userKey}/applications/{applicationName}/watch"
    method = "POST"
    return Request(
        method, 
        url.format(['applicationName', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
