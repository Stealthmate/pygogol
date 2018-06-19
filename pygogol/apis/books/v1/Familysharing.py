from pygogol.core import Request

from Defs import baseUrl

def getFamilyInfo(source=None):
    url = baseUrl + "familysharing/getFamilyInfo"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def share(docId=None, source=None, volumeId=None):
    url = baseUrl + "familysharing/share"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unshare(docId=None, source=None, volumeId=None):
    url = baseUrl + "familysharing/unshare"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
