from pygogol.core import Request

from Defs import baseUrl

def get(volumeId=None, country=None, includeNonComicsSeries=None, partner=None, projection=None, source=None, user_library_consistent_read=None):
    url = baseUrl + "volumes/{volumeId}"
    method = "GET"
    return Request(
        method, 
        url.format(['volumeId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(download=None, filter=None, langRestrict=None, libraryRestrict=None, maxAllowedMaturityRating=None, maxResults=None, orderBy=None, partner=None, printType=None, projection=None, q=None, showPreorders=None, source=None, startIndex=None):
    url = baseUrl + "volumes"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
