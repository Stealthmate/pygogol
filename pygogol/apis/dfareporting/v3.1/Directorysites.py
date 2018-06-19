from pygogol.core import Request

from Defs import baseUrl

def get(id=None, profileId=None):
    url = baseUrl + "userprofiles/{profileId}/directorySites/{id}"
    method = "GET"
    return Request(
        method, 
        url.format(['id', 'profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/directorySites"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, acceptsInStreamVideoPlacements=None, acceptsInterstitialPlacements=None, acceptsPublisherPaidPlacements=None, active=None, countryId=None, dfpNetworkCode=None, ids=None, maxResults=None, pageToken=None, parentId=None, searchString=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/directorySites"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
