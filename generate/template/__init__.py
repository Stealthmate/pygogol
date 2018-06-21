from jinja2 import Template

def loadTemplate(fn):
    asd = ""
    with open(fn) as f:
        asd = f.read()
    return asd

SDK = loadTemplate("./generate/template/SDK.py")
RESOURCE = loadTemplate("./generate/template/Resource.py")
DEFS = loadTemplate("./generate/template/Defs.py")
RESOURCE_JINJA = Template(loadTemplate("./generate/template/jinja/Resource.py"))