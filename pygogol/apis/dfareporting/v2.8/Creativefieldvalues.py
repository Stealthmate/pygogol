from pygogol.core import Request

from Defs import baseUrl

def delete(creativeFieldId=None, id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['creativeFieldId', 'id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(creativeFieldId=None, id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['creativeFieldId', 'id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(creativeFieldId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues"
    method = "POST"
    return Request(
        method, 
        url.format(['creativeFieldId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(creativeFieldId=None, profileId=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues"
    method = "GET"
    return Request(
        method, 
        url.format(['creativeFieldId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(creativeFieldId=None, profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues"
    method = "PATCH"
    return Request(
        method, 
        url.format(['creativeFieldId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(creativeFieldId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/creativeFields/{creativeFieldId}/creativeFieldValues"
    method = "PUT"
    return Request(
        method, 
        url.format(['creativeFieldId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
