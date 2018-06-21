from jinja2 import Template

def loadTemplate(fn):
    asd = ""
    with open(fn) as f:
        asd = f.read()
    return asd

RESOURCE_JINJA = Template(loadTemplate("./generate/template/jinja/Resource.py"))
METHOD_JINJA = Template(loadTemplate("./generate/template/jinja/Method.py"))
DEFS_JINJA = Template(loadTemplate("./generate/template/jinja/Defs.py"))