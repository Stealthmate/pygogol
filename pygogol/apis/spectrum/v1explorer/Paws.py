from pygogol.core import Request

from Defs import baseUrl

def getSpectrum():
    url = baseUrl + "getSpectrum"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getSpectrumBatch():
    url = baseUrl + "getSpectrumBatch"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def init():
    url = baseUrl + "init"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def notifySpectrumUse():
    url = baseUrl + "notifySpectrumUse"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def register():
    url = baseUrl + "register"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verifyDevice():
    url = baseUrl + "verifyDevice"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
