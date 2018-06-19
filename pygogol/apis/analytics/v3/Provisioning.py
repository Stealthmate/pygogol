from pygogol.core import Request

from Defs import baseUrl

def createAccountTicket():
    url = baseUrl + "provisioning/createAccountTicket"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def createAccountTree():
    url = baseUrl + "provisioning/createAccountTree"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
