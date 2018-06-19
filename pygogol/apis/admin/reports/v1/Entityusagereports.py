from pygogol.core import Request

from Defs import baseUrl

def get(date=None, entityKey=None, entityType=None, customerId=None, filters=None, maxResults=None, pageToken=None, parameters=None):
    url = baseUrl + "usage/{entityType}/{entityKey}/dates/{date}"
    method = "GET"
    return Request(
        method, 
        url.format(['date', 'entityKey', 'entityType']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
