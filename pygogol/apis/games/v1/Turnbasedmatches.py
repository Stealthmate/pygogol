from pygogol.core import Request

from Defs import baseUrl

def cancel(matchId=None):
    url = baseUrl + "turnbasedmatches/{matchId}/cancel"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def create(language=None):
    url = baseUrl + "turnbasedmatches/create"
    method = "POST"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def decline(matchId=None, language=None):
    url = baseUrl + "turnbasedmatches/{matchId}/decline"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def dismiss(matchId=None):
    url = baseUrl + "turnbasedmatches/{matchId}/dismiss"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def finish(matchId=None, language=None):
    url = baseUrl + "turnbasedmatches/{matchId}/finish"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def get(matchId=None, includeMatchData=None, language=None):
    url = baseUrl + "turnbasedmatches/{matchId}"
    method = "GET"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def join(matchId=None, language=None):
    url = baseUrl + "turnbasedmatches/{matchId}/join"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def leave(matchId=None, language=None):
    url = baseUrl + "turnbasedmatches/{matchId}/leave"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def leaveTurn(matchId=None, language=None, matchVersion=None, pendingParticipantId=None):
    url = baseUrl + "turnbasedmatches/{matchId}/leaveTurn"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(includeMatchData=None, language=None, maxCompletedMatches=None, maxResults=None, pageToken=None):
    url = baseUrl + "turnbasedmatches"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def rematch(matchId=None, language=None, requestId=None):
    url = baseUrl + "turnbasedmatches/{matchId}/rematch"
    method = "POST"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def sync(includeMatchData=None, language=None, maxCompletedMatches=None, maxResults=None, pageToken=None):
    url = baseUrl + "turnbasedmatches/sync"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def takeTurn(matchId=None, language=None):
    url = baseUrl + "turnbasedmatches/{matchId}/turn"
    method = "PUT"
    return Request(
        method, 
        url.format(['matchId']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
