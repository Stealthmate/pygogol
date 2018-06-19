from pygogol.core import Request

from Defs import baseUrl

def abandonInstances(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/abandonInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteInstances(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/deleteInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instanceGroupManager=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}"
    method = "GET"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listManagedInstances(instanceGroupManager=None, project=None, region=None, filter=None, maxResults=None, order_by=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/listManagedInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def recreateInstances(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/recreateInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resize(instanceGroupManager=None, project=None, region=None, requestId=None, size=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/resize"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setInstanceTemplate(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/setInstanceTemplate"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setTargetPools(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/setTargetPools"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
