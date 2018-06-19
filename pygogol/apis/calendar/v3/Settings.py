from pygogol.core import Request

from Defs import baseUrl

def get(setting=None):
    url = baseUrl + "users/me/settings/{setting}"
    method = "GET"
    return Request(
        method, 
        url.format(['setting']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None, syncToken=None):
    url = baseUrl + "users/me/settings"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(maxResults=None, pageToken=None, syncToken=None):
    url = baseUrl + "users/me/settings/watch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
