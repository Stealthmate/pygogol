from pygogol.core import Request

from Defs import baseUrl

def get(profileId=None, summaryAccountId=None):
    url = baseUrl + "userprofiles/{profileId}/accountActiveAdSummaries/{summaryAccountId}"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId', 'summaryAccountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
