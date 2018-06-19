from pygogol.core import Request

from Defs import baseUrl

def get(fileId=None, reportId=None):
    url = baseUrl + "reports/{reportId}/files/{fileId}"
    method = "GET"
    return Request(
        method, 
        url.format(['fileId', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, maxResults=None, pageToken=None, scope=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/files"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
