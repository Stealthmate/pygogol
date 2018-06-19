from pygogol.core import Request

from Defs import baseUrl

def getPartnersstatus(requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None):
    url = baseUrl + "v2/partnersstatus"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateCompanies(requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None, updateMask=None):
    url = baseUrl + "v2/companies"
    method = "PATCH"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateLeads(requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None, updateMask=None):
    url = baseUrl + "v2/leads"
    method = "PATCH"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
