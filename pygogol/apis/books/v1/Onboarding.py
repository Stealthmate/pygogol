from pygogol.core import Request

from Defs import baseUrl

def listCategories(locale=None):
    url = baseUrl + "onboarding/listCategories"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listCategoryVolumes(categoryId=None, locale=None, maxAllowedMaturityRating=None, pageSize=None, pageToken=None):
    url = baseUrl + "onboarding/listCategoryVolumes"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
