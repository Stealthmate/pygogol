from pygogol.core import Request

from Defs import baseUrl

def check(relation=None, source.androidApp.certificate.sha256Fingerprint=None, source.androidApp.packageName=None, source.web.site=None, target.androidApp.certificate.sha256Fingerprint=None, target.androidApp.packageName=None, target.web.site=None):
    url = baseUrl + "v1/assetlinks:check"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
