from pygogol.core import Request
from json import dumps
from .Defs import baseUrl

def get():
    url = baseUrl + "about"
    method = "GET"
    queryParams = {
        
    }
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format() + "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())),
        {},
        dumps("")
    )
