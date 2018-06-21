from jinja2 import Template

def loadTemplate(fn):
    asd = ""
    with open(fn) as f:
        asd = f.read()
    return asd

RESOURCE = Template(loadTemplate("./generate/template/Resource.py"))
METHOD = Template(loadTemplate("./generate/template/Method.py"))
DEFS = Template(loadTemplate("./generate/template/Defs.py"))