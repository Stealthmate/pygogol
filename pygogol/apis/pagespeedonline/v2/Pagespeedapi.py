from pygogol.core import Request

from Defs import baseUrl

def runpagespeed(filter_third_party_resources=None, locale=None, rule=None, screenshot=None, strategy=None, url=None):
    url = baseUrl + "runPagespeed"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
