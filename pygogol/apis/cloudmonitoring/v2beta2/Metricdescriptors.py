from pygogol.core import Request

from Defs import baseUrl

def create(project=None):
    url = baseUrl + "{project}/metricDescriptors"
    method = "POST"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def delete(metric=None, project=None):
    url = baseUrl + "{project}/metricDescriptors/{metric}"
    method = "DELETE"
    return Request(
        method, 
        url.format(['metric', 'project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def list(project=None, count=None, pageToken=None, query=None):
    url = baseUrl + "{project}/metricDescriptors"
    method = "GET"
    return Request(
        method, 
        url.format(['project']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
