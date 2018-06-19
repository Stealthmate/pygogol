from pygogol.core import Request

from Defs import baseUrl

def allocateIds(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:allocateIds"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def beginTransaction(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:beginTransaction"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def commit(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:commit"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def lookup(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:lookup"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def reserveIds(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:reserveIds"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rollback(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:rollback"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def runQuery(projectId=None):
    url = baseUrl + "v1beta3/projects/{projectId}:runQuery"
    method = "POST"
    return Request(
        method, 
        url.format(['projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
