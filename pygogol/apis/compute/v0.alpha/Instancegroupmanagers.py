from pygogol.core import Request

from Defs import baseUrl

def abandonInstances(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/abandonInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/instanceGroupManagers"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def applyUpdatesToInstances(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/applyUpdatesToInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteInstances(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/deleteInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deletePerInstanceConfigs(instanceGroupManager=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/deletePerInstanceConfigs"
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

def insert(project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listManagedInstances(instanceGroupManager=None, project=None, zone=None, filter=None, maxResults=None, order_by=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/listManagedInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listPerInstanceConfigs(instanceGroupManager=None, project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/listPerInstanceConfigs"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def recreateInstances(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/recreateInstances"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resize(instanceGroupManager=None, project=None, zone=None, requestId=None, size=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/resize"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resizeAdvanced(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/resizeAdvanced"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setAutoHealingPolicies(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setAutoHealingPolicies"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setInstanceTemplate(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setInstanceTemplate"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setTargetPools(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/setTargetPools"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}"
    method = "PUT"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updatePerInstanceConfigs(instanceGroupManager=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instanceGroupManagers/{instanceGroupManager}/updatePerInstanceConfigs"
    method = "POST"
    return Request(
        method, 
        url.format(['instanceGroupManager', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
