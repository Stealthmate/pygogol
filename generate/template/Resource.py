from pygogol.core import Request
from json import dumps
from urllib.parse import quote
from pygogol.apis.{{apiname}}.Defs import baseUrl

{% for m in methods %}
def {{m['methodName']}}({% set params = m['pathParams'] + ([] if m['bodyParam'] is none else [m['bodyParam']]) %}
    {{ params|join(", \n    ") }}{% if m['queryParams']|length > 0 %}{% if params|length > 0 %},
    {% endif %}{% for q in m['queryParams'] %}{{q}}=None{% if not loop.last %},
    {% endif %}{% endfor %}{% endif %}
    ):
    url = baseUrl + "{{m['methodUrl']}}"
    method = "{{m['httpMethod']}}"
    queryParams = {
        {% for q in m['queryParams'] %}"{{q}}": {{q}}{% if not loop.last %}, 
        {% endif %}{% endfor %}
    }
    {% raw %}queryParams = {k: quote(v) for k, v in queryParams.items() if v is not None}
    query = "?" + "&".join(map(lambda x: "{}={}".format(x, queryParams[x]), queryParams.keys())){% endraw %}
    return Request(
        method,
        url.format({% for p in m['pathParams'] %}{{p}}={{p}}{% if not loop.last %}, {% endif %}{% endfor %}) + (query if len(query) > 1 else ""),
        {{'{'}}{% if m['bodyParam'] is not none %}"content-type": "application/json"{% endif %}{{'}'}},
        {% if m['bodyParam'] is not none %}dumps({{m['bodyParam']}}){% else %}None{% endif %}
    )
{% endfor %}

{{methods|join("\n\n")}}