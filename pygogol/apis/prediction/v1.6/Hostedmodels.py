from pygogol.core import Request

from Defs import baseUrl

def predict(hostedModelName=None, project=None):
    url = baseUrl + "{project}/hostedmodels/{hostedModelName}/predict"
    method = "POST"
    return Request(
        method, 
        url.format(['hostedModelName', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
