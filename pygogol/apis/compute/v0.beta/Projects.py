from pygogol.core import Request

from Defs import baseUrl

def disableXpnHost(project=None, requestId=None):
    url = baseUrl + "{project}/disableXpnHost"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def disableXpnResource(project=None, requestId=None):
    url = baseUrl + "{project}/disableXpnResource"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def enableXpnHost(project=None, requestId=None):
    url = baseUrl + "{project}/enableXpnHost"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def enableXpnResource(project=None, requestId=None):
    url = baseUrl + "{project}/enableXpnResource"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None):
    url = baseUrl + "{project}"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getXpnHost(project=None):
    url = baseUrl + "{project}/getXpnHost"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getXpnResources(project=None, filter=None, maxResults=None, order_by=None, pageToken=None):
    url = baseUrl + "{project}/getXpnResources"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listXpnHosts(project=None, filter=None, maxResults=None, order_by=None, pageToken=None):
    url = baseUrl + "{project}/listXpnHosts"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def moveDisk(project=None, requestId=None):
    url = baseUrl + "{project}/moveDisk"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def moveInstance(project=None, requestId=None):
    url = baseUrl + "{project}/moveInstance"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setCommonInstanceMetadata(project=None, requestId=None):
    url = baseUrl + "{project}/setCommonInstanceMetadata"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setDefaultNetworkTier(project=None, requestId=None):
    url = baseUrl + "{project}/setDefaultNetworkTier"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setUsageExportBucket(project=None, requestId=None):
    url = baseUrl + "{project}/setUsageExportBucket"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
