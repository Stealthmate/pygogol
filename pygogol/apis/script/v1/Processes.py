from pygogol.core import Request

from Defs import baseUrl

def list(pageSize=None, pageToken=None, userProcessFilter.deploymentId=None, userProcessFilter.endTime=None, userProcessFilter.functionName=None, userProcessFilter.projectName=None, userProcessFilter.scriptId=None, userProcessFilter.startTime=None, userProcessFilter.statuses=None, userProcessFilter.types=None, userProcessFilter.userAccessLevels=None):
    url = baseUrl + "v1/processes"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )

def listScriptProcesses(pageSize=None, pageToken=None, scriptId=None, scriptProcessFilter.deploymentId=None, scriptProcessFilter.endTime=None, scriptProcessFilter.functionName=None, scriptProcessFilter.startTime=None, scriptProcessFilter.statuses=None, scriptProcessFilter.types=None, scriptProcessFilter.userAccessLevels=None):
    url = baseUrl + "v1/processes:listScriptProcesses"
    method = "GET"
    return Request(
        method, 
        url.format([]) + "?" + "&".join(),
        {},
        jsonDumps()
    )
