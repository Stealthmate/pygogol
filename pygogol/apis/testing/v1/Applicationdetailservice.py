from pygogol.core import Request

from Defs import baseUrl

def getApkDetails():
    url = baseUrl + "v1/applicationDetailService/getApkDetails"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
