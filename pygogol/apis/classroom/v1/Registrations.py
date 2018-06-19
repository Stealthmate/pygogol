from pygogol.core import Request

from Defs import baseUrl

def create():
    url = baseUrl + "v1/registrations"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(registrationId=None):
    url = baseUrl + "v1/registrations/{registrationId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['registrationId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
