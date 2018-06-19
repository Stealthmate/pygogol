from pygogol.core import Request

from Defs import baseUrl

def clear(calendarId=None):
    url = baseUrl + "calendars/{calendarId}/clear"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(calendarId=None):
    url = baseUrl + "calendars/{calendarId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(calendarId=None):
    url = baseUrl + "calendars/{calendarId}"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "calendars"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(calendarId=None):
    url = baseUrl + "calendars/{calendarId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(calendarId=None):
    url = baseUrl + "calendars/{calendarId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
