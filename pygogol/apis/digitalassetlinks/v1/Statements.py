from pygogol.core import Request

from Defs import baseUrl

def list(relation=None, source.androidApp.certificate.sha256Fingerprint=None, source.androidApp.packageName=None, source.web.site=None):
    url = baseUrl + "v1/statements:list"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
