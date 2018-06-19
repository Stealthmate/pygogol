from pygogol.core import Request

from Defs import baseUrl

def claim(milestoneId=None, questId=None, requestId=None):
    url = baseUrl + "quests/{questId}/milestones/{milestoneId}/claim"
    method = "PUT"
    return Request(
        method, 
        url.format(['milestoneId', 'questId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
