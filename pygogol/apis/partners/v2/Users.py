from pygogol.core import Request

from Defs import baseUrl

def createCompanyRelation(userId=None, requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None):
    url = baseUrl + "v2/users/{userId}/companyRelation"
    method = "PUT"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteCompanyRelation(userId=None, requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None):
    url = baseUrl + "v2/users/{userId}/companyRelation"
    method = "DELETE"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(userId=None, requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None, userView=None):
    url = baseUrl + "v2/users/{userId}"
    method = "GET"
    return Request(
        method, 
        url.format(['userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateProfile(requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None):
    url = baseUrl + "v2/users/profile"
    method = "PATCH"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
