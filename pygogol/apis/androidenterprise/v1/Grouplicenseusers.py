from pygogol.core import Request

from Defs import baseUrl

def list(enterpriseId=None, groupLicenseId=None):
    url = baseUrl + "enterprises/{enterpriseId}/groupLicenses/{groupLicenseId}/users"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'groupLicenseId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
