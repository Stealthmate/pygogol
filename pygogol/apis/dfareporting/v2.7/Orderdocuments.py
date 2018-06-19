from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None, projectId=None):
    url = baseUrl + "userprofiles/{profileId}/projects/{projectId}/orderDocuments/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, projectId=None, approved=None, ids=None, maxResults=None, orderId=None, pageToken=None, searchString=None, siteId=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/projects/{projectId}/orderDocuments"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId', 'projectId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
