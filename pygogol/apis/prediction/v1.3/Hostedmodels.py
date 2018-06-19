from pygogol.core import Request

from Defs import baseUrl

def predict(hostedModelName=None):
    url = baseUrl + "hostedmodels/{hostedModelName}/predict"
    method = "POST"
    return Request(
        method, 
        url.format(['hostedModelName']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
