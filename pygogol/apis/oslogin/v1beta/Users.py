from pygogol.core import Request

from Defs import baseUrl

def getLoginProfile(name=None):
    url = baseUrl + "v1beta/{+name}/loginProfile"
    method = "GET"
    return Request(
        method, 
        url.format(['name']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def importSshPublicKey(parent=None, projectId=None):
    url = baseUrl + "v1beta/{+parent}:importSshPublicKey"
    method = "POST"
    return Request(
        method, 
        url.format(['parent']) + "?" + "&".join(),
        {},
        jsonDumps()
    )