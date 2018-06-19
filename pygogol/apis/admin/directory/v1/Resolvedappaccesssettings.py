from pygogol.core import Request

from Defs import baseUrl

def GetSettings():
    url = baseUrl + "resolvedappaccesssettings"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def ListTrustedApps():
    url = baseUrl + "trustedapps"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
