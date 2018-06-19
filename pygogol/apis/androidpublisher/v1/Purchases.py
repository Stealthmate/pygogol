from pygogol.core import Request

from Defs import baseUrl

def cancel(packageName=None, subscriptionId=None, token=None):
    url = baseUrl + "{packageName}/subscriptions/{subscriptionId}/purchases/{token}/cancel"
    method = "POST"
    return Request(
        method, 
        url.format(['packageName', 'subscriptionId', 'token']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(packageName=None, subscriptionId=None, token=None):
    url = baseUrl + "{packageName}/subscriptions/{subscriptionId}/purchases/{token}"
    method = "GET"
    return Request(
        method, 
        url.format(['packageName', 'subscriptionId', 'token']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
