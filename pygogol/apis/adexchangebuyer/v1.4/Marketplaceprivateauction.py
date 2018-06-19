from pygogol.core import Request

from Defs import baseUrl

def updateproposal(privateAuctionId=None):
    url = baseUrl + "privateauction/{privateAuctionId}/updateproposal"
    method = "POST"
    return Request(
        method, 
        url.format(['privateAuctionId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
