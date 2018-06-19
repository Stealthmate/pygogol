from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None, projectId=None):
    url = baseUrl + "userprofiles/{profileId}/projects/{projectId}/inventoryItems/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, projectId=None, ids=None, inPlan=None, maxResults=None, orderId=None, pageToken=None, siteId=None, sortField=None, sortOrder=None, type=None):
    url = baseUrl + "userprofiles/{profileId}/projects/{projectId}/inventoryItems"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
