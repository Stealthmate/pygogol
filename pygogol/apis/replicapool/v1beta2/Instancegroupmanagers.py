from pygogol.core import Request

from Defs import baseUrl

def abandonInstances(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/abandonInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteInstances(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/deleteInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}"
    method = "GET"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, size=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def recreateInstances(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/recreateInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resize(instanceGroupManager=None, project=None, zone=None, size=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/resize"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setInstanceTemplate(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setInstanceTemplate"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setTargetPools(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setTargetPools"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
