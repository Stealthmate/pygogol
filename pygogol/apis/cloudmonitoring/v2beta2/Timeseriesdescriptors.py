from pygogol.core import Request

from Defs import baseUrl

def list(metric=None, project=None, aggregator=None, count=None, labels=None, oldest=None, pageToken=None, timespan=None, window=None, youngest=None):
    url = baseUrl + "{project}/timeseriesDescriptors/{metric}"
    method = "GET"
    return Request(
        method, 
        url.format(['metric', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
