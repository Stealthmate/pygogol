from pygogol.core import Request

from Defs import baseUrl

def get(licenseCode=None, project=None):
    url = baseUrl + "{project}/global/licenseCodes/{licenseCode}"
    method = "GET"
    return Request(
        method, 
        url.format(['licenseCode', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
