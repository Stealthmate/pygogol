from pygogol.core import Request

from Defs import baseUrl

def delete(calendarId=None, eventId=None, sendNotifications=None):
    url = baseUrl + "calendars/{calendarId}/events/{eventId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['calendarId', 'eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(calendarId=None, eventId=None, alwaysIncludeEmail=None, maxAttendees=None, timeZone=None):
    url = baseUrl + "calendars/{calendarId}/events/{eventId}"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId', 'eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def import(calendarId=None, conferenceDataVersion=None, supportsAttachments=None):
    url = baseUrl + "calendars/{calendarId}/events/import"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(calendarId=None, conferenceDataVersion=None, maxAttendees=None, sendNotifications=None, supportsAttachments=None):
    url = baseUrl + "calendars/{calendarId}/events"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def instances(calendarId=None, eventId=None, alwaysIncludeEmail=None, maxAttendees=None, maxResults=None, originalStart=None, pageToken=None, showDeleted=None, timeMax=None, timeMin=None, timeZone=None):
    url = baseUrl + "calendars/{calendarId}/events/{eventId}/instances"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId', 'eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(calendarId=None, alwaysIncludeEmail=None, iCalUID=None, maxAttendees=None, maxResults=None, orderBy=None, pageToken=None, privateExtendedProperty=None, q=None, sharedExtendedProperty=None, showDeleted=None, showHiddenInvitations=None, singleEvents=None, syncToken=None, timeMax=None, timeMin=None, timeZone=None, updatedMin=None):
    url = baseUrl + "calendars/{calendarId}/events"
    method = "GET"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def move(calendarId=None, eventId=None, destination=None, sendNotifications=None):
    url = baseUrl + "calendars/{calendarId}/events/{eventId}/move"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId', 'eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(calendarId=None, eventId=None, alwaysIncludeEmail=None, conferenceDataVersion=None, maxAttendees=None, sendNotifications=None, supportsAttachments=None):
    url = baseUrl + "calendars/{calendarId}/events/{eventId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['calendarId', 'eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def quickAdd(calendarId=None, sendNotifications=None, text=None):
    url = baseUrl + "calendars/{calendarId}/events/quickAdd"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(calendarId=None, eventId=None, alwaysIncludeEmail=None, conferenceDataVersion=None, maxAttendees=None, sendNotifications=None, supportsAttachments=None):
    url = baseUrl + "calendars/{calendarId}/events/{eventId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['calendarId', 'eventId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def watch(calendarId=None, alwaysIncludeEmail=None, iCalUID=None, maxAttendees=None, maxResults=None, orderBy=None, pageToken=None, privateExtendedProperty=None, q=None, sharedExtendedProperty=None, showDeleted=None, showHiddenInvitations=None, singleEvents=None, syncToken=None, timeMax=None, timeMin=None, timeZone=None, updatedMin=None):
    url = baseUrl + "calendars/{calendarId}/events/watch"
    method = "POST"
    return Request(
        method, 
        url.format(['calendarId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
