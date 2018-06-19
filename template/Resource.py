def {resourceName}({params}):
    url = baseUrl + "{resourceUrl}"
    method = "{resourceMethod}"
    queryParams = {{
        {queryParams}
    }}
    queryParams = dict( filter(lambda x: queryParams[x] is not None, queryParams.keys()) )
    return Request(
        method, 
        url.format({pathParams}) + "?" + "&".join(map(lambda x: "{{}}={{}}".format(x, queryParams[x]), queryParams.keys())),
        {{}},
        dumps({bodyParam})
    )
