from pygogol.core import Request

from Defs import baseUrl

def acknowledgeNotificationSet(notificationSetId=None):
    url = baseUrl + "enterprises/acknowledgeNotificationSet"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def completeSignup(completionToken=None, enterpriseToken=None):
    url = baseUrl + "enterprises/completeSignup"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def createWebToken(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/createWebToken"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def enroll(token=None):
    url = baseUrl + "enterprises/enroll"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generateSignupUrl(callbackUrl=None):
    url = baseUrl + "enterprises/signupUrl"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getAndroidDevicePolicyConfig(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/androidDevicePolicyConfig"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getServiceAccount(enterpriseId=None, keyType=None):
    url = baseUrl + "enterprises/{enterpriseId}/serviceAccount"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getStoreLayout(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(token=None):
    url = baseUrl + "enterprises"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(domain=None):
    url = baseUrl + "enterprises"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def pullNotificationSet(requestMode=None):
    url = baseUrl + "enterprises/pullNotificationSet"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def sendTestPushNotification(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/sendTestPushNotification"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setAccount(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/account"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setAndroidDevicePolicyConfig(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/androidDevicePolicyConfig"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def setStoreLayout(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/storeLayout"
    method = "PUT"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def unenroll(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/unenroll"
    method = "POST"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
