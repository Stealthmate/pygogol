from pygogol.core import Request

from Defs import baseUrl

def insert(campaignId=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations"
    method = "POST"
    return Request(
        method, 
        url.format(['campaignId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(campaignId=None, profileId=None, maxResults=None, pageToken=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/campaigns/{campaignId}/campaignCreativeAssociations"
    method = "GET"
    return Request(
        method, 
        url.format(['campaignId', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
