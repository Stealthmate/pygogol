from pygogol.core import Request

from Defs import baseUrl

def addAccessConfig(instance=None, project=None, zone=None, networkInterface=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/addAccessConfig"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def aggregatedList(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/aggregated/instances"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def attachDisk(instance=None, project=None, zone=None, forceAttach=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/attachDisk"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteAccessConfig(instance=None, project=None, zone=None, accessConfig=None, networkInterface=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/deleteAccessConfig"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def detachDisk(instance=None, project=None, zone=None, deviceName=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/detachDisk"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(instance=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getSerialPortOutput(instance=None, project=None, zone=None, port=None, start=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/serialPort"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, zone=None, requestId=None, sourceInstanceTemplate=None):
    url = baseUrl + "{project}/zones/{zone}/instances"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instances"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listReferrers(instance=None, project=None, zone=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/referrers"
    method = "GET"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reset(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/reset"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setDeletionProtection(project=None, resource=None, zone=None, deletionProtection=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{resource}/setDeletionProtection"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setDiskAutoDelete(instance=None, project=None, zone=None, autoDelete=None, deviceName=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setDiskAutoDelete"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setLabels(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setLabels"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setMachineResources(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setMachineResources"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setMachineType(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setMachineType"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setMetadata(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setMetadata"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setMinCpuPlatform(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setMinCpuPlatform"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setScheduling(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setScheduling"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setServiceAccount(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setServiceAccount"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setShieldedVmIntegrityPolicy(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setShieldedVmIntegrityPolicy"
    method = "PATCH"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setTags(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/setTags"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def simulateMaintenanceEvent(instance=None, project=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/simulateMaintenanceEvent"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def start(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/start"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def startWithEncryptionKey(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/startWithEncryptionKey"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def stop(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/stop"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def testIamPermissions(project=None, resource=None, zone=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{resource}/testIamPermissions"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'resource', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateAccessConfig(instance=None, project=None, zone=None, networkInterface=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/updateAccessConfig"
    method = "POST"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateNetworkInterface(instance=None, project=None, zone=None, networkInterface=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/updateNetworkInterface"
    method = "PATCH"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateShieldedVmConfig(instance=None, project=None, zone=None, requestId=None):
    url = baseUrl + "{project}/zones/{zone}/instances/{instance}/updateShieldedVmConfig"
    method = "PATCH"
    return Request(
        method, 
        url.format(['instance', 'project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
