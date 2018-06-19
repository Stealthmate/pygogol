from pygogol.core import Request

from Defs import baseUrl

def allocateQuota(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:allocateQuota"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def check(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:check"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def endReconciliation(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:endReconciliation"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def releaseQuota(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:releaseQuota"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def report(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:report"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def startReconciliation(serviceName=None):
    url = baseUrl + "v1/services/{serviceName}:startReconciliation"
    method = "POST"
    return Request(
        method, 
        url.format(['serviceName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
