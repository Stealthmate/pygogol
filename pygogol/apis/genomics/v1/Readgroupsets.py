from pygogol.core import Request

from Defs import baseUrl

def delete(readGroupSetId=None):
    url = baseUrl + "v1/readgroupsets/{readGroupSetId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['readGroupSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def export(readGroupSetId=None):
    url = baseUrl + "v1/readgroupsets/{readGroupSetId}:export"
    method = "POST"
    return Request(
        method, 
        url.format(['readGroupSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(readGroupSetId=None):
    url = baseUrl + "v1/readgroupsets/{readGroupSetId}"
    method = "GET"
    return Request(
        method, 
        url.format(['readGroupSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def import():
    url = baseUrl + "v1/readgroupsets:import"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def patch(readGroupSetId=None, updateMask=None):
    url = baseUrl + "v1/readgroupsets/{readGroupSetId}"
    method = "PATCH"
    return Request(
        method, 
        url.format(['readGroupSetId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def search():
    url = baseUrl + "v1/readgroupsets/search"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
