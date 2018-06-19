from pygogol.core import Request

from Defs import baseUrl

def delete(firewall=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/firewalls/{firewall}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['firewall', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(firewall=None, project=None):
    url = baseUrl + "{project}/global/firewalls/{firewall}"
    method = "GET"
    return Request(
        method, 
        url.format(['firewall', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None, requestId=None):
    url = baseUrl + "{project}/global/firewalls"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/firewalls"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(firewall=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/firewalls/{firewall}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['firewall', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(firewall=None, project=None, requestId=None):
    url = baseUrl + "{project}/global/firewalls/{firewall}"
    method = "PUT"
    return Request(
        method, 
        url.format(['firewall', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
