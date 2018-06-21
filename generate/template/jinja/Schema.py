def {{schema}}(
    {% for p in properties %}{{p}}=None{% if not loop.last %},
    {% endif %}{% endfor %}{% endif %}
    ):
    return {
        {% for p in properties %}"{{p}}"={{p}}{% if not loop.last %},
        {% endif %}{% endfor %}{% endif %}
    }