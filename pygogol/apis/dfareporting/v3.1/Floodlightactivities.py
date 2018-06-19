from pygogol.core import Request

from Defs import baseUrl

def delete(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities/{id}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def generatetag(profileId=None, floodlightActivityId=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities/generatetag"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, advertiserId=None, floodlightActivityGroupIds=None, floodlightActivityGroupName=None, floodlightActivityGroupTagString=None, floodlightActivityGroupType=None, floodlightConfigurationId=None, ids=None, maxResults=None, pageToken=None, searchString=None, sortField=None, sortOrder=None, tagString=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, id=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/floodlightActivities"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
