from pygogol.core import Request

from Defs import baseUrl

def clear(tasklist=None):
    url = baseUrl + "lists/{tasklist}/clear"
    method = "POST"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(task=None, tasklist=None):
    url = baseUrl + "lists/{tasklist}/tasks/{task}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['task', 'tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(task=None, tasklist=None):
    url = baseUrl + "lists/{tasklist}/tasks/{task}"
    method = "GET"
    return Request(
        method, 
        url.format(['task', 'tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(tasklist=None, parent=None, previous=None):
    url = baseUrl + "lists/{tasklist}/tasks"
    method = "POST"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(tasklist=None, completedMax=None, completedMin=None, dueMax=None, dueMin=None, maxResults=None, pageToken=None, showCompleted=None, showDeleted=None, showHidden=None, updatedMin=None):
    url = baseUrl + "lists/{tasklist}/tasks"
    method = "GET"
    return Request(
        method, 
        url.format(['tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def move(task=None, tasklist=None, parent=None, previous=None):
    url = baseUrl + "lists/{tasklist}/tasks/{task}/move"
    method = "POST"
    return Request(
        method, 
        url.format(['task', 'tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(task=None, tasklist=None):
    url = baseUrl + "lists/{tasklist}/tasks/{task}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['task', 'tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(task=None, tasklist=None):
    url = baseUrl + "lists/{tasklist}/tasks/{task}"
    method = "PUT"
    return Request(
        method, 
        url.format(['task', 'tasklist']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
