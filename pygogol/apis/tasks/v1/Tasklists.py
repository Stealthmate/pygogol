from pygogol.core import Request

from Defs import baseUrl

def delete(tasklist=None):
    url = baseUrl + "users/@me/lists/{tasklist}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(tasklist=None):
    url = baseUrl + "users/@me/lists/{tasklist}"
    method = "GET"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "users/@me/lists"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(maxResults=None, pageToken=None):
    url = baseUrl + "users/@me/lists"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(tasklist=None):
    url = baseUrl + "users/@me/lists/{tasklist}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(tasklist=None):
    url = baseUrl + "users/@me/lists/{tasklist}"
    method = "PUT"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
