from pygogol.core import Request

from Defs import baseUrl

def get(companyId=None, address=None, currencyCode=None, orderBy=None, requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None, view=None):
    url = baseUrl + "v2/companies/{companyId}"
    method = "GET"
    return Request(
        method, 
        url.format(['companyId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(address=None, companyName=None, gpsMotivations=None, industries=None, languageCodes=None, maxMonthlyBudget.currencyCode=None, maxMonthlyBudget.nanos=None, maxMonthlyBudget.units=None, minMonthlyBudget.currencyCode=None, minMonthlyBudget.nanos=None, minMonthlyBudget.units=None, orderBy=None, pageSize=None, pageToken=None, requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None, services=None, specializations=None, view=None, websiteUrl=None):
    url = baseUrl + "v2/companies"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
