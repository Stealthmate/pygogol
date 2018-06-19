from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, task=None, taskqueue=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks/{task}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'task', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, task=None, taskqueue=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks/{task}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'task', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, taskqueue=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def lease(project=None, taskqueue=None, groupByTag=None, leaseSecs=None, numTasks=None, tag=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks/lease"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, taskqueue=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, task=None, taskqueue=None, newLeaseSeconds=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks/{task}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'task', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, task=None, taskqueue=None, newLeaseSeconds=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}/tasks/{task}"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'task', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )