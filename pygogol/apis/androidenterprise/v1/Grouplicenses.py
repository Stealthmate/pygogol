from pygogol.core import Request

from Defs import baseUrl

def get(enterpriseId=None, groupLicenseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/groupLicenses/{groupLicenseId}"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'groupLicenseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(enterpriseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/groupLicenses"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
