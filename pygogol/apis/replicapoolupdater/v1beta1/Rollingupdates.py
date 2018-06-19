from pygogol.core import Request

from Defs import baseUrl

def cancel(project=None, rollingUpdate=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/cancel"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'rollingUpdate', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, rollingUpdate=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates/{rollingUpdate}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'rollingUpdate', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listInstanceUpdates(project=None, rollingUpdate=None, zone=None, filter=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/instanceUpdates"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'rollingUpdate', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def pause(project=None, rollingUpdate=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/pause"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'rollingUpdate', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resume(project=None, rollingUpdate=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/resume"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'rollingUpdate', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rollback(project=None, rollingUpdate=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/rollingUpdates/{rollingUpdate}/rollback"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'rollingUpdate', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
