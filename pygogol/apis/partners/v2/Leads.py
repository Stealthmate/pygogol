from pygogol.core import Request

from Defs import baseUrl

def list(orderBy=None, pageSize=None, pageToken=None, requestMetadata.experimentIds=None, requestMetadata.locale=None, requestMetadata.partnersSessionId=None, requestMetadata.trafficSource.trafficSourceId=None, requestMetadata.trafficSource.trafficSubId=None, requestMetadata.userOverrides.ipAddress=None, requestMetadata.userOverrides.userId=None):
    url = baseUrl + "v2/leads"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
