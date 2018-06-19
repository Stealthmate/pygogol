def {resourceName}({params}):
    url = baseUrl + "{resourceUrl}"
    method = "{resourceMethod}"
    queryParams = {{
        {queryParams}
    }}
    queryParams = {{k: quote(v) for k, v in queryParams.items() if v is not None}}
    query = "?" + "&".join(map(lambda x: "{{}}={{}}".format(x, queryParams[x]), queryParams.keys()))
    return Request(
        method, 
        url.format({pathParams}) + (query if len(query) > 1 else ""),
        {{}},
        {bodyParam}
    )
