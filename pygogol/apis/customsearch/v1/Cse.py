from pygogol.core import Request

from Defs import baseUrl

def list(c2coff=None, cr=None, cx=None, dateRestrict=None, exactTerms=None, excludeTerms=None, fileType=None, filter=None, gl=None, googlehost=None, highRange=None, hl=None, hq=None, imgColorType=None, imgDominantColor=None, imgSize=None, imgType=None, linkSite=None, lowRange=None, lr=None, num=None, orTerms=None, q=None, relatedSite=None, rights=None, safe=None, searchType=None, siteSearch=None, siteSearchFilter=None, sort=None, start=None):
    url = baseUrl + "v1"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
