from pygogol.core import Request

from Defs import baseUrl

def get(project=None, taskqueue=None, getStats=None):
    url = baseUrl + "{project}/taskqueues/{taskqueue}"
    method = "GET"
    return Request(
        method, 
        url.format(['project', 'taskqueue']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
