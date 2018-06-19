from pygogol.core import Request

from Defs import baseUrl

def delete(forwardingRule=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/forwardingRules/{forwardingRule}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['forwardingRule', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(forwardingRule=None, project=None):
    url = baseUrl + "{project}/global/forwardingRules/{forwardingRule}"
    method = "GET"
    return Request(
        method, 
        url.format(['forwardingRule', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/forwardingRules"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/forwardingRules"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setTarget(forwardingRule=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/forwardingRules/{forwardingRule}/setTarget"
    method = "POST"
    return Request(
        method, 
        url.format(['forwardingRule', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
