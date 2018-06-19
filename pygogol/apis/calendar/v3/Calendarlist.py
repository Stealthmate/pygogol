from pygogol.core import Request

from Defs import baseUrl

def delete(calendarId=None):
    url = baseUrl + "users/me/calendarList/{calendarId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(calendarId=None):
    url = baseUrl + "users/me/calendarList/{calendarId}"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(colorRgbFormat=None):
    url = baseUrl + "users/me/calendarList"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, minAccessRole=None, pageToken=None, showDeleted=None, showHidden=None, syncToken=None):
    url = baseUrl + "users/me/calendarList"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(calendarId=None, colorRgbFormat=None):
    url = baseUrl + "users/me/calendarList/{calendarId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(calendarId=None, colorRgbFormat=None):
    url = baseUrl + "users/me/calendarList/{calendarId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(maxResults=None, minAccessRole=None, pageToken=None, showDeleted=None, showHidden=None, syncToken=None):
    url = baseUrl + "users/me/calendarList/watch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
