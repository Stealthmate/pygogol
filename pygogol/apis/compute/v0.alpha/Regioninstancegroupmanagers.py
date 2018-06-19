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

def applyUpdatesToInstances(instanceGroupManager=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/applyUpdatesToInstances"
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

def deletePerInstanceConfigs(instanceGroupManager=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/deletePerInstanceConfigs"
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

def listPerInstanceConfigs(instanceGroupManager=None, project=None, region=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/listPerInstanceConfigs"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}"
    method = "PATCH"
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

def setAutoHealingPolicies(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/setAutoHealingPolicies"
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

def testIamPermissions(project=None, region=None, resource=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'region', 'resource']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(instanceGroupManager=None, project=None, region=None, requestId=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}"
    method = "PUT"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updatePerInstanceConfigs(instanceGroupManager=None, project=None, region=None):
    url = baseUrl + "{project}/regions/{region}/instanceGroupManagers/{instanceGroupManager}/updatePerInstanceConfigs"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'region']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
