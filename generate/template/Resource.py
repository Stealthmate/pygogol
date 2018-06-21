def {resourceName}({params}):
    url = baseUrl + "{resourceUrl}"
    method = "{resourceMethod}"
    queryParams = {{
        {queryParams}
    }}
    queryParams = {{k: quote(v) for k, v in queryParams.items() if v is not None}}
    query = "?" + "&".join(map(lambda x: "{{}}={{}}".format(x, queryParams[x]), queryParams.keys()))
    print("Body", {bodyParam})
    return Request(
        method, 
        url.format({pathParams}) + (query if len(query) > 1 else ""),
        {{
            "content-type": "application/json"
        }},
        {bodyParam}
    )
