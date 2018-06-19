from pygogol.core import Request

from Defs import baseUrl

def list(drive.ancestorId=None, drive.fileId=None, groupingStrategy=None, pageSize=None, pageToken=None, source=None, userId=None):
    url = baseUrl + "activities"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
