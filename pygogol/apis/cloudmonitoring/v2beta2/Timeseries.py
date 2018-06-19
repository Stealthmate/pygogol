from pygogol.core import Request

from Defs import baseUrl

def list(metric=None, project=None, aggregator=None, count=None, labels=None, oldest=None, pageToken=None, timespan=None, window=None, youngest=None):
    url = baseUrl + "{project}/timeseries/{metric}"
    method = "GET"
    return Request(
        method, 
        url.format(['metric', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def write(project=None):
    url = baseUrl + "{project}/timeseries:write"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
