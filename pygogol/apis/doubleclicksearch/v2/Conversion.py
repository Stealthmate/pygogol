from pygogol.core import Request

from Defs import baseUrl

def get(advertiserId=None, agencyId=None, engineAccountId=None, adGroupId=None, adId=None, campaignId=None, criterionId=None, endDate=None, rowCount=None, startDate=None, startRow=None):
    url = baseUrl + "agency/{agencyId}/advertiser/{advertiserId}/engine/{engineAccountId}/conversion"
    method = "GET"
    return Request(
        method, 
        url.format(['advertiserId', 'agencyId', 'engineAccountId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert():
    url = baseUrl + "conversion"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(advertiserId=None, agencyId=None, endDate=None, engineAccountId=None, rowCount=None, startDate=None, startRow=None):
    url = baseUrl + "conversion"
    method = "PATCH"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update():
    url = baseUrl + "conversion"
    method = "PUT"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateAvailability():
    url = baseUrl + "conversion/updateAvailability"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
