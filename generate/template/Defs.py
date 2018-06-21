baseUrl = "{{baseUrl}}"
{% for s in scopes %}
SCOPE_{{s[0]}} = "{{s[1]}}"{% endfor %}

{% for (s, v) in schemas.items() %}
def {{ s }}(
    {% for p in v["properties"] %}{{ p }}=None{% if not loop.last %},
    {% endif %}{% endfor %}
    ):
    return {
        {% for p in v["properties"] %}"{{p}}": {{p}}{% if not loop.last %},
        {% endif %}{% endfor %}
    }
{% endfor %}