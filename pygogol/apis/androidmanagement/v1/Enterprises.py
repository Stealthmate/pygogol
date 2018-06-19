from pygogol.core import Request

from Defs import baseUrl

def create(enterpriseToken=None, projectId=None, signupUrlName=None):
    url = baseUrl + "v1/enterprises"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(name=None):
    url = baseUrl + "v1/{+name}"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(name=None, updateMask=None):
    url = baseUrl + "v1/{+name}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
