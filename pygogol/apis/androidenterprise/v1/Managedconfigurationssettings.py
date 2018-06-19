from pygogol.core import Request

from Defs import baseUrl

def list(enterpriseId=None, productId=None):
    url = baseUrl + "enterprises/{enterpriseId}/products/{productId}/managedConfigurationsSettings"
    method = "GET"
    return Request(
        method, 
        url.format(['enterpriseId', 'productId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
