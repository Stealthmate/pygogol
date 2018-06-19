from pygogol.core import Request

from Defs import baseUrl

def get(surveyUrlId=None):
    url = baseUrl + "surveys/{surveyUrlId}/results"
    method = "GET"
    return Request(
        method, 
        url.format(['surveyUrlId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
