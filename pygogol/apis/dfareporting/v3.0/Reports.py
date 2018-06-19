from pygogol.core import Request

from Defs import baseUrl

def delete(profileId=None, reportId=None):
    url = baseUrl + "userprofiles/{profileId}/reports/{reportId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['profileId', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(profileId=None, reportId=None):
    url = baseUrl + "userprofiles/{profileId}/reports/{reportId}"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(profileId=None):
    url = baseUrl + "userprofiles/{profileId}/reports"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(profileId=None, maxResults=None, pageToken=None, scope=None, sortField=None, sortOrder=None):
    url = baseUrl + "userprofiles/{profileId}/reports"
    method = "GET"
    return Request(
        method, 
        url.format(['profileId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(profileId=None, reportId=None):
    url = baseUrl + "userprofiles/{profileId}/reports/{reportId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['profileId', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def run(profileId=None, reportId=None, synchronous=None):
    url = baseUrl + "userprofiles/{profileId}/reports/{reportId}/run"
    method = "POST"
    return Request(
        method, 
        url.format(['profileId', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(profileId=None, reportId=None):
    url = baseUrl + "userprofiles/{profileId}/reports/{reportId}"
    method = "PUT"
    return Request(
        method, 
        url.format(['profileId', 'reportId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
