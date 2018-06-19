from pygogol.core import Request

from Defs import baseUrl

def insert(collection=None, userId=None):
    url = baseUrl + "people/{userId}/media/{collection}"
    method = "POST"
    return Request(
        method, 
        url.format(['collection', 'userId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
