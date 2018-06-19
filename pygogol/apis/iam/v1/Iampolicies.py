from pygogol.core import Request

from Defs import baseUrl

def queryAuditableServices():
    url = baseUrl + "v1/iamPolicies:queryAuditableServices"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
