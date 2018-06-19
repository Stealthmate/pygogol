from pygogol.core import Request

from Defs import baseUrl

def activate(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}/activate"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def changePlan(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}/changePlan"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def changeRenewalSettings(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}/changeRenewalSettings"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def changeSeats(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}/changeSeats"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(customerId=None, subscriptionId=None, deletionType=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}"
    method = "GET"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def insert(customerId=None, customerAuthToken=None):
    url = baseUrl + "customers/{customerId}/subscriptions"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(customerAuthToken=None, customerId=None, customerNamePrefix=None, maxResults=None, pageToken=None):
    url = baseUrl + "subscriptions"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def startPaidService(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}/startPaidService"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def suspend(customerId=None, subscriptionId=None):
    url = baseUrl + "customers/{customerId}/subscriptions/{subscriptionId}/suspend"
    method = "POST"
    return Request(
        method, 
        url.format(['customerId', 'subscriptionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
