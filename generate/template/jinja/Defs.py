baseUrl = "{{baseUrl}}"
{% for s in scopes %}
SCOPE_{{s[0]}} = "{{s[1]}}"{% endfor %}
