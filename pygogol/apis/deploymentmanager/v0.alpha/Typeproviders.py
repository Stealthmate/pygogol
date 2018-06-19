from pygogol.core import Request

from Defs import baseUrl

def delete(project=None, typeProvider=None):
    url = baseUrl + "{project}/global/typeProviders/{typeProvider}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['project', 'typeProvider']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(project=None, typeProvider=None):
    url = baseUrl + "{project}/global/typeProviders/{typeProvider}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'typeProvider']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getType(project=None, type=None, typeProvider=None):
    url = baseUrl + "{project}/global/typeProviders/{typeProvider}/types/{type}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'type', 'typeProvider']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(project=None):
    url = baseUrl + "{project}/global/typeProviders"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/typeProviders"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listTypes(project=None, typeProvider=None, filter=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/global/typeProviders/{typeProvider}/types"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'typeProvider']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(project=None, typeProvider=None):
    url = baseUrl + "{project}/global/typeProviders/{typeProvider}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['project', 'typeProvider']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(project=None, typeProvider=None):
    url = baseUrl + "{project}/global/typeProviders/{typeProvider}"
    method = "PUT"
    return Request(
        method, 
        url.format(['project', 'typeProvider']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
