from pygogol.core import Request

from Defs import baseUrl

def delete(calendarId=None, ruleId=None):
    url = baseUrl + "calendars/{calendarId}/acl/{ruleId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['calendarId', 'ruleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(calendarId=None, ruleId=None):
    url = baseUrl + "calendars/{calendarId}/acl/{ruleId}"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId', 'ruleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(calendarId=None, sendNotifications=None):
    url = baseUrl + "calendars/{calendarId}/acl"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(calendarId=None, maxResults=None, pageToken=None, showDeleted=None, syncToken=None):
    url = baseUrl + "calendars/{calendarId}/acl"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(calendarId=None, ruleId=None, sendNotifications=None):
    url = baseUrl + "calendars/{calendarId}/acl/{ruleId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['calendarId', 'ruleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(calendarId=None, ruleId=None, sendNotifications=None):
    url = baseUrl + "calendars/{calendarId}/acl/{ruleId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['calendarId', 'ruleId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(calendarId=None, maxResults=None, pageToken=None, showDeleted=None, syncToken=None):
    url = baseUrl + "calendars/{calendarId}/acl/watch"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
