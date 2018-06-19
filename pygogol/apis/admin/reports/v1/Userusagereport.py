from pygogol.core import Request

from Defs import baseUrl

def get(date=None, userKey=None, customerId=None, filters=None, maxResults=None, pageToken=None, parameters=None):
    url = baseUrl + "usage/users/{userKey}/dates/{date}"
    method = "GET"
    return Request(
        method, 
        url.format(['date', 'userKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
