from pygogol.core import Request

from Defs import baseUrl

def getUserSettings():
    url = baseUrl + "myconfig/getUserSettings"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def releaseDownloadAccess(cpksver=None, locale=None, source=None, volumeIds=None):
    url = baseUrl + "myconfig/releaseDownloadAccess"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def requestAccess(cpksver=None, licenseTypes=None, locale=None, nonce=None, source=None, volumeId=None):
    url = baseUrl + "myconfig/requestAccess"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def syncVolumeLicenses(cpksver=None, features=None, includeNonComicsSeries=None, locale=None, nonce=None, showPreorders=None, source=None, volumeIds=None):
    url = baseUrl + "myconfig/syncVolumeLicenses"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateUserSettings():
    url = baseUrl + "myconfig/updateUserSettings"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
