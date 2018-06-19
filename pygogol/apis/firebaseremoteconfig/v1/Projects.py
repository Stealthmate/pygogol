from pygogol.core import Request

from Defs import baseUrl

def getRemoteConfig(project=None):
    url = baseUrl + "v1/{+project}/remoteConfig"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateRemoteConfig(project=None, validateOnly=None):
    url = baseUrl + "v1/{+project}/remoteConfig"
    method = "PUT"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
