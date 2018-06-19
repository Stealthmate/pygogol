from pygogol.core import Request

from Defs import baseUrl

def createAuthUri():
    url = baseUrl + "createAuthUri"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteAccount():
    url = baseUrl + "deleteAccount"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def downloadAccount():
    url = baseUrl + "downloadAccount"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def emailLinkSignin():
    url = baseUrl + "emailLinkSignin"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getAccountInfo():
    url = baseUrl + "getAccountInfo"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getOobConfirmationCode():
    url = baseUrl + "getOobConfirmationCode"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getProjectConfig(delegatedProjectNumber=None, projectNumber=None):
    url = baseUrl + "getProjectConfig"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getPublicKeys():
    url = baseUrl + "publicKeys"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getRecaptchaParam():
    url = baseUrl + "getRecaptchaParam"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def resetPassword():
    url = baseUrl + "resetPassword"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def sendVerificationCode():
    url = baseUrl + "sendVerificationCode"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setAccountInfo():
    url = baseUrl + "setAccountInfo"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setProjectConfig():
    url = baseUrl + "setProjectConfig"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def signOutUser():
    url = baseUrl + "signOutUser"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def signupNewUser():
    url = baseUrl + "signupNewUser"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def uploadAccount():
    url = baseUrl + "uploadAccount"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verifyAssertion():
    url = baseUrl + "verifyAssertion"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verifyCustomToken():
    url = baseUrl + "verifyCustomToken"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verifyPassword():
    url = baseUrl + "verifyPassword"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def verifyPhoneNumber():
    url = baseUrl + "verifyPhoneNumber"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
