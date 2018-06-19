from pygogol.core import Request

from Defs import baseUrl

def list(profileId=None, countryDartIds=None, dartIds=None, namePrefix=None, regionDartIds=None):
    url = baseUrl + "userprofiles/{profileId}/cities"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
