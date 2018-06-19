from pygogol.core import Request

from Defs import baseUrl

def addBook(drive_document_id=None, mime_type=None, name=None, upload_client_token=None):
    url = baseUrl + "cloudloading/addBook"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def deleteBook(volumeId=None):
    url = baseUrl + "cloudloading/deleteBook"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def updateBook():
    url = baseUrl + "cloudloading/updateBook"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
