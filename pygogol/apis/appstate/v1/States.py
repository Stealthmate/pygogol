from pygogol.core import Request

from Defs import baseUrl

def clear(stateKey=None, currentDataVersion=None):
    url = baseUrl + "states/{stateKey}/clear"
    method = "POST"
    return Request(
        method, 
        url.format(['stateKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(stateKey=None):
    url = baseUrl + "states/{stateKey}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['stateKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(stateKey=None):
    url = baseUrl + "states/{stateKey}"
    method = "GET"
    return Request(
        method, 
        url.format(['stateKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(includeData=None):
    url = baseUrl + "states"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def update(stateKey=None, currentStateVersion=None):
    url = baseUrl + "states/{stateKey}"
    method = "PUT"
    return Request(
        method, 
        url.format(['stateKey']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
