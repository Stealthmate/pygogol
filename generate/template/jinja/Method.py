def {{methodName}}({% set params = pathParams + ([] if bodyParam is none else [bodyParam]) %}
    {{ params|join(", \n    ") }}{% if queryParams|length > 0 %}{% if params|length > 0 %},
    {% endif %}{% for q in queryParams %}{{q}}=None{% if not loop.last %},
    {% endif %}{% endfor %}{% endif %}
    ):
    url = baseUrl + "{{methodUrl}}"
    method = "{{httpMethod}}"
    queryParams = {
        {% for q in queryParams %}"{{q}}": {{q}}{% if not loop.last %}, 
        {% endif %}{% endfor %}
    }
    {% raw %}queryParams = {k: quote(v) for k, v in queryParams.items() if v is not None}
    query = "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())){% endraw %}
    return Request(
        method,
        url.format({{pathParams|join(", ")}}) + (query if len(query) > 1 else ""),
        {{'{'}}{% if bodyParam is not none %}"content-type": "application/json"{% endif %}{{'}'}},
        {% if bodyParam is not none %}dumps({{bodyParam}}){% else %}None{% endif %}
    )