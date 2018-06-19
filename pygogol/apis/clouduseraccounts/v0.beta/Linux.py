from pygogol.core import Request

from Defs import baseUrl

def getAuthorizedKeysView(project=None, user=None, zone=None, instance=None, login=None):
    url = baseUrl + "{project}/zones/{zone}/authorizedKeysView/{user}"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'user', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def getLinuxAccountViews(project=None, zone=None, filter=None, instance=None, maxResults=None, orderBy=None, pageToken=None):
    url = baseUrl + "{project}/zones/{zone}/linuxAccountViews"
    method = "POST"
    return Request(
        method, 
        url.format(['project', 'zone']) + "?" + "&".join(),
        {},
        jsonDumps()
    )
