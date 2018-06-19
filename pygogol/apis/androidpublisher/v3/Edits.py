from pygogol.core import Request

from Defs import baseUrl

def commit(editId=None, packageName=None):
    url = baseUrl + "{packageName}/edits/{editId}:commit"
    method = "POST"
    return Request(
        method, 
        url.format(['editId', 'packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(editId=None, packageName=None):
    url = baseUrl + "{packageName}/edits/{editId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['editId', 'packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(editId=None, packageName=None):
    url = baseUrl + "{packageName}/edits/{editId}"
    method = "GET"
    return Request(
        method, 
        url.format(['editId', 'packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(packageName=None):
    url = baseUrl + "{packageName}/edits"
    method = "POST"
    return Request(
        method, 
        url.format(['packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def validate(editId=None, packageName=None):
    url = baseUrl + "{packageName}/edits/{editId}:validate"
    method = "POST"
    return Request(
        method, 
        url.format(['editId', 'packageName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
