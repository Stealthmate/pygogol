from pygogol.core import Request

from Defs import baseUrl

def delete(objectId=None, profileId=None, name=None, objectType=None):
    url = baseUrl + "userprofiles/{profileId}/dynamicTargetingKeys/{objectId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['objectId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/dynamicTargetingKeys"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, advertiserId=None, names=None, objectId=None, objectType=None):
    url = baseUrl + "userprofiles/{profileId}/dynamicTargetingKeys"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
